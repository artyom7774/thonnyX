
from PIL import ImageGrab

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

from tasks.turtle import color as create

import typing

if typing.TYPE_CHECKING:
    from turtle import *


tracer(0)

colormode(255)
color(*create((0, 0, 0)))
left(90)
forward(100)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(50)

penup()
goto(0, 0)
right(180)
color(0, 0, 0)
pendown()

tracer(1)



    
done()

