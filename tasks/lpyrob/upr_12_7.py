#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells

class Task:
    CHECKS = 1

    def load_level(self, n):
        rob.set_field_size(9, 5)
        rob.set_parking_cell(1, 1)
        

        rob.set_cell_type(1, 1, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(1, 2, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(1, 3, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(2, 1, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(2, 3, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(3, 1, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(3, 3, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(4, 2, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(5, 1, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(5, 3, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(6, 1, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(6, 3, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(7, 1, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(7, 2, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(7, 3, rob.CELL_TO_BE_FILLED)

        
        
        rob.goto(1, 1)

    def check_solution(self):
        if not rob.is_parking_point():
            return False

        return check_filled_cells([(1, 1), (1, 2), (1, 3),
                                   (2, 1), (2,3),
                                   (3, 1), (3, 3), (4, 2), (5, 1), (5, 3),
                                   (6, 1), (6,3),
                                   (7, 1), (7, 2), (7, 3)])
