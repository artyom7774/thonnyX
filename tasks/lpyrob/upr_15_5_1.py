#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells, find_cells_to_be_filled
import random

class Task:
    CHECKS = 6

    def load_level(self, n):
        rob.set_field_size(7, 7)
        x = random.randint(0, 1)
        if x == 1:
            k1 = random.randint(0, 6)
        else:
            k1 = 6
        k2 = random.randint(0, 6)
        if k1 != 6:
            rob.set_parking_cell(k1 + 1, k2)
            rob.set_cell_type(k1 + 1, k2, rob.CELL_TO_BE_FILLED)
        else:
            rob.set_parking_cell(k1, k2)            
        
        self.cells_to_fill = find_cells_to_be_filled()
        rob.goto(k1, k2)

    def check_solution(self):
        if not rob.is_parking_point():
            return False
        return check_filled_cells(self.cells_to_fill)
