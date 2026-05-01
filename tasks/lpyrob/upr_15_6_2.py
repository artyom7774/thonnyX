#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells, find_cells_to_be_filled
import random

class Task:
    CHECKS = 6

    def load_level(self, n):
        rob.set_field_size(2, 2)        

        x = random.randint(0, 3)        
        
        if x == 0:            
            rob.set_cell_type(1, 1, rob.CELL_TO_BE_FILLED) 
            rob.goto(0, 0)
            rob.set_parking_cell(1, 1)
        elif x == 1:            
            rob.set_cell_type(1, 0, rob.CELL_TO_BE_FILLED) 
            rob.goto(0, 1)
            rob.set_parking_cell(1, 0)
        elif x == 2:            
            rob.set_cell_type(0, 1, rob.CELL_TO_BE_FILLED) 
            rob.goto(1, 0)
            rob.set_parking_cell(0, 1)
        else:            
            rob.set_cell_type(0, 0, rob.CELL_TO_BE_FILLED) 
            rob.goto(1, 1)
            rob.set_parking_cell(0, 0)

        self.cells_to_fill = find_cells_to_be_filled()
       

    def check_solution(self):
        if not rob.is_parking_point():
            return False
        return check_filled_cells(self.cells_to_fill)
