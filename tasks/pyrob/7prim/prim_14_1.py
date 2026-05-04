#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells, find_cells_to_be_filled

class Task:
    CHECKS = 1

    def load_level(self, n):
        rob.set_field_size(3, 3)
        rob.set_parking_cell(1, 1)

        rob.set_cell_type(1, 1, rob.CELL_FILLED)  
        rob.goto(1,1)
        rob.put_wall(left = True, top = True)

               
        rob.goto(1, 1)

    def check_solution(self):
        if not rob.is_parking_point():
            return False

        return check_filled_cells([(1, 1)])
