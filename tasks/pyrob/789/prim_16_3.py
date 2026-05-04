#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells, find_cells_to_be_filled
import random

class Task:
    CHECKS = 4

    def load_level(self, n):
        dl = random.randint(8, 20)
        rob.set_field_size(9, dl)        
        rob.goto(0, 0)
        
        for i in range(4):
            for j in range (dl - 1):
                rob.put_wall(bottom = True)
                rob.move_right()
            rob.move_down()
            for j in range (dl - 1):
                rob.put_wall(bottom = True)
                rob.move_left()
            rob.move_down()
        
        rob.set_parking_cell(8, 0)
        rob.goto(0, 0)

    def check_solution(self):
        return rob.is_parking_point()
