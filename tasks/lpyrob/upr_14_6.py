#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells, find_cells_to_be_filled
import random

class Task:
    CHECKS = 5

    def load_level(self, n):
        dl = random.randint(12, 20)
        rob.set_field_size(dl, dl)
        k1 = random.randint(1, dl - 7)
        k2 = random.randint(k1 + 3, dl - 3)
        r1 = random.randint(1, dl - 3)
        r2 = random.randint(1, dl - 3)
        rob.set_parking_cell(dl - 1, dl - 1)
               
        for i in range(dl - 1, r1 - 1, -1):
            rob.goto(i, k1)
            if i != r1:
                rob.put_wall(left = True)
            rob.set_cell_type(i, k1, rob.CELL_TO_BE_FILLED)
            rob.set_cell_type(i, k1 - 1, rob.CELL_TO_BE_FILLED)
        
        for i in range(dl - 1, r2 - 1, -1):
            rob.goto(i, k2)
            if i != r2:
                rob.put_wall(left = True)
            rob.set_cell_type(i, k2, rob.CELL_TO_BE_FILLED)
            rob.set_cell_type(i, k2 - 1, rob.CELL_TO_BE_FILLED)
       
        self.cells_to_fill = find_cells_to_be_filled()
        rob.goto(dl - 1, 0)

    def check_solution(self):
        if not rob.is_parking_point():
            return False
        return check_filled_cells(self.cells_to_fill)
