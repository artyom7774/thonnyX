#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells, find_cells_to_be_filled

class Task:
    CHECKS = 1

    def load_level(self, n):
        rob.set_field_size(4, 7)
        rob.set_parking_cell(0, 0)
        

        rob.set_cell_type(2, 2, rob.CELL_FILLED)
        rob.set_cell_type(2, 3, rob.CELL_FILLED)
        rob.set_cell_type(0, 2, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(0, 3, rob.CELL_TO_BE_FILLED)
       # self.cells_to_be_filled = find_cells_to_be_filled()
        
        for i in range(1, 5):
            rob.goto(0, i)
            rob.put_wall(bottom = True)

        rob.goto(1, 1)


    def check_solution(self):
        if not rob.is_parking_point():
            return False
        return check_filled_cells([(2,2),(2,3),(0,2),(0,3)])
