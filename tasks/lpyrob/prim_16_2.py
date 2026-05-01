#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells, find_cells_to_be_filled
import random

class Task:
    CHECKS = 6

    def load_level(self, n):
        rob.set_field_size(10, 20)        
        k = random.randint(3, 16)
        rob.goto(9, k)
        h = random.randint(3, 7)
        for i in range(h):
            rob.put_wall(right = True, left = True)
            rob.move_up()
        x = random.randint(0, 1)
        if x == 0:
            rob.put_wall(right = True, top = True)
            rob.move_left()
            w = random.randint(1, k - 2)
            for i in range(w):
                rob.put_wall(top = True, bottom = True)
                rob.move_left()
            rob.put_wall(left = True, top = True, bottom = True)
            pos = rob.get_pos()
            rob.set_parking_cell(pos[0], pos[1])
        else:
            rob.put_wall(left = True, top = True)
            w = random.randint(1, 20 - k - 3)
            rob.move_right()
            for i in range(w):
                rob.put_wall(top = True, bottom = True)
                rob.move_right()
            rob.put_wall(right = True, top = True, bottom = True)
            pos = rob.get_pos()
            rob.set_parking_cell(pos[0], pos[1])
        
               
        rob.goto(1, 0)

        rob.goto(9, k)

    def check_solution(self):
        return rob.is_parking_point()
