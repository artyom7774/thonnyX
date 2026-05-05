from tasks.turtle import color as create

import typing

if typing.TYPE_CHECKING:
    from turtle import *

tracer(0)

colormode(255)
color(*create((0, 0, 0)))

penup()
goto(0, 0)
color(0, 0, 0)
speed(1)
pendown()

tracer(1)
