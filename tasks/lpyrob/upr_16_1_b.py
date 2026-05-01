#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells, find_cells_to_be_filled
import random

class Task:
    CHECKS = 6

    def load_level(self, n):
        dl = random.randint(9, 15)
        rob.set_field_size(3, dl)
        k = random.randint(3, dl - 2)
        rob.goto(1, 0)
        for i in range(1, k):
            rob.set_cell_type(1, i, rob.CELL_FILLED)
            rob.move_right()
            
       
        rob.set_parking_cell(1, 0)
        rob.goto(1, k - 1)

    def check_solution(self):
        return rob.is_parking_point()

