#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells

class Task:
    CHECKS = 1

    def load_level(self, n):
        rob.set_field_size(3, 3)
        rob.set_parking_cell(0, 0)
        

        rob.set_cell_type(0, 0, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(0, 1, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(0, 2, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(1, 0, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(1, 2, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(2, 0, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(2, 1, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(2, 2, rob.CELL_TO_BE_FILLED)

        rob.goto(0, 0)

    def check_solution(self):
        if not rob.is_parking_point():
            return False

        return check_filled_cells([(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)])
