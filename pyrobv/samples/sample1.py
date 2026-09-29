#!/usr/bin/python3

from pyrobv.api import *


@task
def example1():

    for i in range(9):
        move_right()
        move_down()

run_tasks(verbose=True)
