#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells, find_cells_to_be_filled

class Task:
    CHECKS = 1

    def load_level(self, n):
        rob.set_field_size(11, 11)
        rob.set_parking_cell(0, 10)

        for i in range (10):
          rob.set_cell_type(i, i, rob.CELL_TO_BE_FILLED)
          rob.set_cell_type(i, 10 - i, rob.CELL_TO_BE_FILLED)
        self.cells_to_be_filled = find_cells_to_be_filled()
      
        
        rob.goto(0, 0)

    def check_solution(self):
        if not rob.is_parking_point():
            return False

        return check_filled_cells(self.cells_to_be_filled)
