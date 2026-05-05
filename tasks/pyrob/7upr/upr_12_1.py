#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells

class Task:
    CHECKS = 1

    def load_level(self, n):
        rob.set_field_size(3, 5)
        rob.set_parking_cell(0, 4)
        

        #rob.set_cell_type(0, 0, rob.CELL_FILLED)
        #rob.set_cell_type(0, 1, rob.CELL_FILLED)
        #rob.set_cell_type(0, 2, rob.CELL_FILLED)
        #rob.set_cell_type(0, 3, rob.CELL_FILLED)
        #rob.set_cell_type(0, 4, rob.CELL_FILLED)

        rob.goto(0, 1)
        rob.put_wall(left=True, bottom=True)
        rob.goto(1, 2)
        rob.put_wall(left=True, bottom=True, right=True)
        rob.goto(0, 3)
        rob.put_wall(bottom=True, right=True)

        rob.goto(0, 0)
    def check_solution(self):
     #   if not rob.is_parking_point():
            return rob.is_parking_point()

       # return check_filled_cells([(0, 0), (1, 1), (2, 2), (1, 3), (0, 4)])
