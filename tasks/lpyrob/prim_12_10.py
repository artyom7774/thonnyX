#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells

class Task:
    CHECKS = 1

    def load_level(self, n):
        rob.set_field_size(4, 7)
        rob.set_parking_cell(0, 0)
        

        rob.set_cell_type(0, 1, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(0, 2, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(0, 3, rob.CELL_TO_BE_FILLED)
        rob.set_cell_type(0, 4, rob.CELL_TO_BE_FILLED)

        for i in range(0, 5):
            rob.goto(0, i)
            rob.put_wall(bottom = True)

        rob.goto(1, 1)


    def check_solution(self):
        if not rob.is_parking_point():
            return False

        return check_filled_cells([(0, 1),(0, 2),(0, 3),(0, 4)])
