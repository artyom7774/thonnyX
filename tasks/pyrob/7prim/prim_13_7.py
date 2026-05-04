#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells, find_cells_to_be_filled



class Task:
    CHECKS = 1

    def load_level(self, n):
        rob.set_field_size(2, 11)
        rob.set_parking_cell(0, 0)
        
        for k in range(2):
            for i in range (1, 11):
                rob.set_cell_type(k, i, rob.CELL_TO_BE_FILLED)
        
        self.cells_to_be_filled = find_cells_to_be_filled()
        
        for i in range(1, 10, 2):
           rob.goto(0, i)
           rob.put_wall(right = True)
        for i in range(0, 11, 2):
           rob.goto(1, i)
           rob.put_wall(right = True)  
        
        rob.goto(0, 10)

    def check_solution(self):
        if not rob.is_parking_point():
            return False

        return check_filled_cells(self.cells_to_be_filled)
