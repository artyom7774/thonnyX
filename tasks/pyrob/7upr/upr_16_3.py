#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells, find_cells_to_be_filled
import random

class Task:
    CHECKS = 4

    def load_level(self, n):
        dl = random.randint(9, 20)
        rob.set_field_size(9, dl)        
        rob.goto(0, 0)
        l = dl - 1
        for i in range(1, 5):
            for j in range (l):
                rob.put_wall(bottom = True)
                pos = rob.get_pos()
                rob.set_cell_type(pos[0], pos[1], rob.CELL_TO_BE_FILLED)
                rob.move_right()
            if not rob.wall_right():
                rob.put_wall(right = True)
            pos = rob.get_pos()
            rob.set_cell_type(pos[0], pos[1], rob.CELL_TO_BE_FILLED)
            rob.move_down()            
            if not rob.wall_right():
                rob.put_wall(right = True)
            
            for j in range (l - 1):
                rob.put_wall(bottom = True)
                pos = rob.get_pos()
                rob.set_cell_type(pos[0], pos[1], rob.CELL_TO_BE_FILLED)
                rob.move_left()            
            rob.put_wall(left = True)
            pos = rob.get_pos()
            rob.set_cell_type(pos[0], pos[1], rob.CELL_TO_BE_FILLED)
            rob.move_down()
            rob.put_wall(left = True)
            l -= 2
         
        for i in range (l + 1):            
            pos = rob.get_pos()
            rob.set_cell_type(pos[0], pos[1], rob.CELL_TO_BE_FILLED)
            rob.move_right()
            
        self.cells_to_fill = find_cells_to_be_filled()    
        rob.goto(8, dl - 4)
        rob.put_wall(left = True)  
        rob.set_parking_cell(8, dl - 5)
        rob.goto(0, 0)

    def check_solution(self):
        return rob.is_parking_point() and check_filled_cells(self.cells_to_fill)
