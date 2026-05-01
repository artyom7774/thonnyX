from tasks.turtle import color as create

import typing

if typing.TYPE_CHECKING:
    from turtle import *

tracer(0)

colormode(255)
color(*create((0, 0, 0)))

forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(180)
forward(100)
right(90)
forward(50)

penup()
goto(0, 0)
right(0)
color(0, 0, 0)
pendown()

tracer(1)
