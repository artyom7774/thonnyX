# TODO ge

import traceback
import threading
import requests
import socket
import json
import time

TITLE = "Thonny X"


class variables:
    VERSION_CAN_BE_UPDATED = False
    VERSION_EXISTS = False

    SOCKET_WAS_CREATED = False

    NEW_VERSION = "none"

    SPEED_CAPACITY = 1

    PYROBO_MODE = False
    TURTLE_MODE = False
    TASKS_MODE = False

    TURTLE_MENU_INFORMATION_LINK = None
    ROROBO_MENU_INFORMATION_LINK = None
    TASKS_MENU_INFORMATION_LINK = None

    RUN_INFORMATION = {
        "turtle": {},

        "pyrob": {},
        "tasks": {}
    }

    NOTEBOOK = None
    CONTENT_TEXT = ""

    TASKS_PATH_BY_NAME = {}

    TURTLE_TASK = ""
    PYROBO_TASK = ""
    TASK = ""


def getStringVersion(version):
    version = version[1:]
    return ''.join(version.split("."))


with open("version.json", "r", encoding="utf-8") as file:
    data = json.load(file)

VERSION = data["version"]

url = "https://raw.githubusercontent.com/Nrdnan/thonnyX-data/main/version.json"
response = requests.get(url)

new = json.loads(response.text) if response.status_code == 200 else None

print(new)

print(time.time(), data["time"], time.time() - data["time"], time.time() - data["time"] > eval(new["update"]))

if new is not None:
    if getStringVersion(VERSION) < getStringVersion(new["version"]):
        variables.VERSION_EXISTS = True

        if time.time() - data["time"] > eval(new["update"]):
            variables.VERSION_CAN_BE_UPDATED = True

variables.NEW_VERSION = new["version"]

s1 = "\n"
s2 = "\t"

generatePyrobCode = lambda task, code: f"""
from pyrob import *

import traceback

@task
def {task}():
{s2}try:
{s2}{s2}pass
{s1.join([s2 + s2 + line for line in code.split(s1)])}
{s2}except Exception as e:
{s2}{s2}traceback.print_exc()

run({variables.SPEED_CAPACITY})
"""

generateTurtleCode = lambda task, code, start: f"""
from turtle import *
import tkinter as tk

COLOR1 = "#EFEFEF"  # dark
COLOR2 = "#F3F3F3"  # light


def create_template():
    setup(660, 660)
    
    root = getscreen()._root
    root.resizable(False, False)
    root.attributes("-topmost", True)
    
    canvas = getcanvas()
    
    cell_size = 25
    half_width = 325
    half_height = 325

    for x in range(-half_width, half_width + 1, cell_size):
        canvas.create_line(x, -half_height, x, half_height, fill=COLOR2, width=1, tags="grid", capstyle=tk.BUTT, smooth=False)

    for y in range(-half_height, half_height + 1, cell_size):
        canvas.create_line(-half_width, y, half_width, y, fill=COLOR2, width=1, tags="grid", capstyle=tk.BUTT, smooth=False)

    canvas.create_line(-half_width, 0, half_width, 0, fill=COLOR1, width=2, tags="axes", capstyle=tk.BUTT, smooth=False)
    canvas.create_line(0, -half_height, 0, half_height, fill=COLOR1, width=2, tags="axes", capstyle=tk.BUTT, smooth=False)

    mark_size = 6

    for x in range(-half_width, half_width + 1, cell_size):
        if x != 0:
            canvas.create_line(x, -mark_size//2, x, mark_size//2, fill=COLOR1, width=1, tags="marks", capstyle=tk.BUTT, smooth=False)

    for y in range(-half_height, half_height + 1, cell_size):
        if y != 0:
            canvas.create_line(-mark_size//2, y, mark_size//2, y, fill=COLOR1, width=1, tags="marks", capstyle=tk.BUTT, smooth=False)
        
    update()
        
    return canvas


canvas = create_template()

{start}

pencolor((0, 0, 0))
pendown()

{code}

done()

"""

generateErrorTaskCode = lambda code, tasks: f"""
import sys

tasks = {tasks.split(s1)}

def input(prompt=""):
    if prompt:
        sys.stdout.write(prompt)
    
    if not tasks:
        print("Неверный формат данных")
        
        exit(0)
    
    return tasks.pop(0)

{code}

"""


def work():
    print("CREATE WORK")

    sock = socket.socket()
    sock.bind(("", 3521))
    sock.listen(1)

    while True:
        conn, addr = sock.accept()

        try:
            data = conn.recv(1024)

            if not data:
                continue

            status = int(data.decode())

            print(status)

            if variables.PYROBO_MODE:
                if variables.PYROBO_TASK not in variables.RUN_INFORMATION["pyrob"]:
                    variables.RUN_INFORMATION["pyrob"][variables.PYROBO_TASK] = 0

                variables.RUN_INFORMATION["pyrob"][variables.PYROBO_TASK] |= status

            print(variables.RUN_INFORMATION["pyrob"])

            import tkinter

            if variables.PYROBO_MODE:
                variables.ROROBO_MENU_INFORMATION_LINK.delete(0, tkinter.END)

            for name, complete in variables.RUN_INFORMATION["pyrob"].items():
                variables.ROROBO_MENU_INFORMATION_LINK.add_command(label=f"{name}: {('-', '+')[complete]}")

        except Exception as e:
            print(traceback.format_exc())

        finally:
            conn.close()

    sock.close()


def update():
    while True:
        time.sleep(1 / 60)

        if variables.NOTEBOOK is None:
            continue

        variables.CONTENT_TEXT = variables.NOTEBOOK.get_current_editor_content()


if not variables.SOCKET_WAS_CREATED:
    thr = threading.Thread(target=lambda: work())
    thr.daemon = True
    thr.start()

    thr = threading.Thread(target=lambda: update())
    thr.daemon = True
    thr.start()

    variables.SOCKET_WAS_CREATED = True
