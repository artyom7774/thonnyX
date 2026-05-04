#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells, find_cells_to_be_filled
import random

class Task:
    CHECKS = 4

    def load_level(self, n):
        rob.set_field_size(7, 7)
        k = random.randint(0, 1)
        
        rob.set_parking_cell(3, 4)
        if k == 1:            
            for i in range(3):
                rob.goto(i, 3)
                rob.put_wall(left = True)
            rob.goto(3, 3)
            rob.put_wall(right = True, top = True)
        else:
            for i in range(3):
                rob.goto(i + 4, 3)
                rob.put_wall(left = True) 
            rob.goto(3, 3)
            rob.put_wall(right = True, bottom = True)
            
        rob.set_cell_type(3, 4, rob.CELL_TO_BE_FILLED)
        self.cells_to_fill = find_cells_to_be_filled()
        rob.goto(3, 2)

    def check_solution(self):
        if not rob.is_parking_point():
            return False
        return check_filled_cells(self.cells_to_fill)
