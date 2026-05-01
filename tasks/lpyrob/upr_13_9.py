#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells, find_cells_to_be_filled

class Task:
    CHECKS = 1

    def load_level(self, n):
        rob.set_field_size(9, 9)
        rob.set_parking_cell(4, 0)

        for i in range (5):
          rob.set_cell_type(i + 4, i, rob.CELL_TO_BE_FILLED)
        for i in range (4):
          rob.set_cell_type(4 - i, i, rob.CELL_TO_BE_FILLED)
        for i in range (4):
          rob.set_cell_type(i, i + 4, rob.CELL_TO_BE_FILLED)
        for i in range (4):
          rob.set_cell_type(i + 4, 8 - i, rob.CELL_TO_BE_FILLED)  
        self.cells_to_be_filled = find_cells_to_be_filled()
      
        
        rob.goto(4, 0)

    def check_solution(self):
        if not rob.is_parking_point():
            return False

        return check_filled_cells(self.cells_to_be_filled)
