#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells

class Task:
    CHECKS = 1

    def load_level(self, n):
        rob.set_field_size(3, 7)
        rob.set_parking_cell(1, 3)
        

        rob.set_cell_type(0, 1, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(0, 4, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(0, 5, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(0, 6, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(1, 0, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(1, 1, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(1, 2, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(1, 4, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(1, 6, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(2, 1, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(2, 4, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(2, 5, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(2, 6, rob.CELL_TO_BE_FILLED)
        
        rob.goto(1, 3)

    def check_solution(self):
        if not rob.is_parking_point():
            return False

        return check_filled_cells([(0, 1), (0, 4), (0, 5), (0, 6),
                                   (1, 0), (1, 1), (1, 2), (1, 4), (1, 6),
                                   (2, 1), (2, 4), (2, 5), (2, 6)])
