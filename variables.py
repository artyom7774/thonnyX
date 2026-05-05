# TODO ge

import traceback
import threading
import socket
import time

TITLE = "Thonny X"
VERSION = "1.1.4"


class variables:
    SOCKET_WAS_CREATED = False

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

{code}
    
done()

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
