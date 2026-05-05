#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells, find_cells_to_be_filled
import random

class Task:
    CHECKS = 6

    def load_level(self, n):
        ld = random.randint(5, 20)
        rob.set_field_size(3, ld)        
        k = random.randint(2, ld - 1)
        rob.goto(1, k)
        rob.put_wall(right = True)
        rob.set_parking_cell(1, k)
        
        for i in range(1, k + 1):
            x = random.randint(0, 2)    
            if x == 1:
                rob.set_cell_type(1, i, rob.CELL_TO_BE_FILLED)
                rob.goto(1, i)
                rob.put_wall(top = True, bottom = True)
            elif x == 0:
                rob.goto(1, i)
                rob.put_wall(bottom = True)
            else:
                rob.goto(1, i)
                rob.put_wall(top = True)
        
        rob.goto(1, 0)
        self.cells_to_fill = find_cells_to_be_filled()
       

    def check_solution(self):
        if not rob.is_parking_point():
            return False
        return check_filled_cells(self.cells_to_fill)
