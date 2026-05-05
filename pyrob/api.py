#!/usr/bin/python3

from pyrob.core import move_left, move_right, move_up, move_down

from pyrob.core import wall_is_above, wall_is_beneath, wall_is_on_the_left, wall_is_on_the_right

from pyrob.core import fill_cell, cell_is_filled

from pyrob.core import mov
from pyrob import task
from pyrob import run_tasks

left = lt = move_left
right = rt = move_right
up = move_up
down = dn = move_down

wall_left = w_left = wlt = wall_is_on_the_left
wall_right = w_right = wrt = wall_is_on_the_right
wall_up = w_up = wup = wall_is_above
wall_down = w_down = wdn = wall_is_beneath

fill = fill_cell
filled = is_fill = cell_is_filled

run = run_tasks
