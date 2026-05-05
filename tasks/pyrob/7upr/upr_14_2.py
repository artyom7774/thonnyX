#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells, find_cells_to_be_filled
import random

class Task:
    CHECKS = 5

    def load_level(self, n):
        dl = random.randint(2, 10) 
        rob.set_field_size(2, dl * 2 + 1)
        rob.set_parking_cell(0, dl * 2)
        
        for i in range (0, dl * 2, 2):
            rob.set_cell_type(0, i, rob.CELL_TO_BE_FILLED)
            rob.set_cell_type(1, i + 1, rob.CELL_TO_BE_FILLED)
        self.cells_to_fill = find_cells_to_be_filled()
               
        rob.goto(0, 0)

    def check_solution(self):
        if not rob.is_parking_point():
            return False
        return check_filled_cells(self.cells_to_fill)
