#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells

class Task:
    CHECKS = 1

    def load_level(self, n):
        rob.set_field_size(2, 4)
        rob.set_parking_cell(0, 3)
        

        rob.set_cell_type(0, 0, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(0, 1, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(0, 2, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(0, 3, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(1, 0, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(1, 1, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(1, 2, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(1, 3, rob.CELL_TO_BE_FILLED)

        rob.goto(0, 0)
        rob.put_wall(right=True)
        rob.goto(0, 2)
        rob.put_wall(right=True)
        rob.goto(1, 1)
        rob.put_wall(right=True)
                
        rob.goto(0, 0)

    def check_solution(self):
        if not rob.is_parking_point():
            return False

        return check_filled_cells([(0, 0), (0, 1), (0, 2), (0, 3),
                                   (1, 0), (1, 1), (1, 2), (1, 3)])
