#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells, find_cells_to_be_filled
import random

class Task:
    CHECKS = 4

    def load_level(self, n):
        dl = random.randint(5, 15)
        rob.set_field_size(dl, dl + 1)        
        rob.goto(0, 0)
        for i in range(dl):
            rob.goto(i, 0)  
            for j in range (1, i + 2):
                pos = rob.get_pos()
                rob.set_cell_type(pos[0], pos[1], rob.CELL_TO_BE_FILLED)
                if not rob.wall_is_on_the_right():
                    rob.move_right()
                   
                   
        self.cells_to_fill = find_cells_to_be_filled()    
        rob.set_parking_cell(0, 0)
        rob.goto(dl - 1, dl - 1)

    def check_solution(self):
        return rob.is_parking_point() and check_filled_cells(self.cells_to_fill)
