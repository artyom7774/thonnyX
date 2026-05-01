#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells, find_cells_to_be_filled
import random

class Task:
    CHECKS = 6

    def load_level(self, n):
        dl = random.randint(9, 15)
        rob.set_field_size(9, dl)
        k = random.randint(3, dl - 2)
        rob.goto(1, k)
        d = random.randint(1, 6)
        for i in range(d):
            rob.put_wall(left = True)
            rob.set_cell_type(i + 1, k, rob.CELL_TO_BE_FILLED)
            rob.move_down()
            
        self.cells_to_fill = find_cells_to_be_filled()
        rob.set_parking_cell(d + 1, k)
        rob.goto(1, k)

    def check_solution(self):
        if not rob.is_parking_point():
            return False
        return check_filled_cells(self.cells_to_fill)

