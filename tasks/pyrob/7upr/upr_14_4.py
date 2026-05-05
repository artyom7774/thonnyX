#!/usr/bin/python3

import pyrob.core as rob
#from tasks.pyrob import check_filled_cells, find_cells_to_be_filled
import random

class Task:
    CHECKS = 5

    def load_level(self, n):
        dl = random.randint(2, 10) 
        rob.set_field_size(dl, dl)
        rob.set_parking_cell(dl - 1, dl - 1)
        
        rob.goto(0, 0)

    def check_solution(self):
        
            return rob.is_parking_point()
   
