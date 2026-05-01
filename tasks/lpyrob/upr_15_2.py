#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells, find_cells_to_be_filled
import random

class Task:
    CHECKS = 1

    def load_level(self, n):
        rob.set_field_size(5, 5)
        rob.set_parking_cell(0, 0)
#        rob.set_cell_type(2, 2, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(2, 3, rob.CELL_FILLED)
        rob.goto(2, 2)
        rob.put_wall(left = True, bottom = True)
        rob.goto(2, 3)
        rob.put_wall(right = True)
        rob.goto(0, 2)
        rob.put_wall(bottom = True)
        
        self.cells_to_fill = find_cells_to_be_filled()
        rob.goto(2, 2)

    def check_solution(self):
        if not rob.is_parking_point():
            return False
        return check_filled_cells(self.cells_to_fill)
