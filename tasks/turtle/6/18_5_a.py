from tasks.turtle import color as create

import typing

if typing.TYPE_CHECKING:
    from turtle import *

tracer(0)

colormode(255)
color(*create((0, 0, 0)))

for i in range(4):
    forward(100)
    left(90)

penup()
goto(0, 0)
right(180)
color(0, 0, 0)
pendown()

tracer(1)
