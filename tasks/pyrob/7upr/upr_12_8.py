#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells

class Task:
    CHECKS = 1

    def load_level(self, n):
        rob.set_field_size(3, 4)
        rob.set_parking_cell(2, 3)
        

        rob.set_cell_type(2, 1, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(2, 2, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(2, 3, rob.CELL_TO_BE_FILLED)
        for i in range(3):
           rob.goto(2, i)
           rob.put_wall(right = True)
           rob.move_up() 
           rob.put_wall(right = True)
        
        rob.goto(2, 0)

    def check_solution(self):
        if not rob.is_parking_point():
            return False

        return check_filled_cells([(2, 1), (2, 2), (2, 3)])
