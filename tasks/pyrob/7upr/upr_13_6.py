#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells, find_cells_to_be_filled

class Task:
    CHECKS = 1

    def load_level(self, n):
        rob.set_field_size(3, 11)
        rob.set_parking_cell(2, 10)

        rob.set_cell_type(0, 10, rob.CELL_TO_BE_FILLED)
        for i in range (5):
          rob.set_cell_type(0, 2 * i, rob.CELL_TO_BE_FILLED)
          rob.set_cell_type(2, 2 * i + 1, rob.CELL_TO_BE_FILLED)
        
        self.cells_to_be_filled = find_cells_to_be_filled()
        for i in range (5):
            rob.goto(0, 2 * i + 2)
            rob.put_wall(left = True)
            rob.goto(2, 2 * i + 1)
            rob.put_wall(left = True)
        
        rob.goto(0, 10)

    def check_solution(self):
        if not rob.is_parking_point():
            return False

        return check_filled_cells(self.cells_to_be_filled)
