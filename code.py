from turtle import *

speed(11)


def p(x, y):
    pu(), setup(x, y)
    pd(), seth(0)


def fc(x1, y1, r1, c1):
    p(x, y), color(c1)
    dot(r1)


x = -200
y = -180
r = 10
colormode(255)
c = 255
while x <= 200:
    fc(x, y, r, (0, c, 0))

    x = x + 10

    c = c - 5

