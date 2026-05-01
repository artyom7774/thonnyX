from tasks.turtle import color as create

import typing

if typing.TYPE_CHECKING:
    from turtle import *

tracer(0)

colormode(255)
color(*create((0, 0, 0)))

for i in range(4):
    forward(100 * ((i % 2 == 0) + 1))
    left(90)

penup()
goto(0, 0)
right(0)
color(0, 0, 0)
pendown()

tracer(1)
