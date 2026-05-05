#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells, find_cells_to_be_filled
import random

class Task:
    CHECKS = 6

    def load_level(self, n):
        rob.set_field_size(5, 5)
        rob.set_parking_cell(2, 2)

        x = random.randint(0, 3)   
        if x == 1:
            rob.set_cell_type(2, 1, rob.CELL_TO_BE_FILLED) 
            rob.goto(2, 1)
            rob.put_wall(left = True)
            rob.set_cell_type(1, 2, rob.CELL_TO_BE_FILLED) 
            rob.goto(1, 2)
            rob.put_wall(top = True)           
            rob.set_cell_type(2, 3, rob.CELL_TO_BE_FILLED) 
            rob.goto(2, 3)
            rob.put_wall(right = True)
            rob.set_cell_type(3, 2, rob.CELL_TO_BE_FILLED) 
            rob.goto(3, 2)
            rob.put_wall(bottom = True)
        else:    
            x = random.randint(0, 1)        
            if x == 1:            
                rob.set_cell_type(2, 1, rob.CELL_TO_BE_FILLED) 
                rob.goto(2, 1)
                rob.put_wall(left = True)
            x = random.randint(0, 1)        
            if x == 1:            
                rob.set_cell_type(1, 2, rob.CELL_TO_BE_FILLED) 
                rob.goto(1, 2)
                rob.put_wall(top = True)           
            x = random.randint(0, 1)        
            if x == 1:            
                rob.set_cell_type(2, 3, rob.CELL_TO_BE_FILLED) 
                rob.goto(2, 3)
                rob.put_wall(right = True)
            x = random.randint(0, 1)        
            if x == 1:            
                rob.set_cell_type(3, 2, rob.CELL_TO_BE_FILLED) 
                rob.goto(3, 2)
                rob.put_wall(bottom = True)

        rob.goto(2, 2)
        rob.set_cell_type(2, 2, rob.CELL_TO_BE_FILLED) 
        self.cells_to_fill = find_cells_to_be_filled()
       

    def check_solution(self):
        if not rob.is_parking_point():
            return False
        return check_filled_cells(self.cells_to_fill)
