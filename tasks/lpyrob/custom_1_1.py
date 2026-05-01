#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells, find_cells_to_be_filled
import random


class Task:
    CHECKS = 5

    def load_level(self, n):
        rows = random.randint(5, 10)
        cols = random.randint(5, 10)
        rob.set_field_size(rows, cols)

        # Старт и парковка
        start_r, start_c = 0, 0
        pr = random.randint(0, rows - 1)
        pc = random.randint(0, cols - 1)
        rob.set_parking_cell(pr, pc)
        rob.set_cell_type(pr, pc, rob.CELL_FILLED)
        self.cells_to_fill = find_cells_to_be_filled()

        # Генерация пути (простейший вариант — прямой коридор)
        path = []
        r, c = start_r, start_c
        while r != pr or c != pc:
            path.append((r, c))
            if r < pr:
                r += 1
            elif r > pr:
                r -= 1
            elif c < pc:
                c += 1
            elif c > pc:
                c -= 1
        path.append((pr, pc))

        # Добавляем случайные стены вне пути
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in path:
                    rob.goto(r, c)
                    # С вероятностью 40% ставим случайную стену
                    if random.random() < 0.4:
                        wall_dir = random.choice(["top", "bottom", "left", "right"])
                        if wall_dir == "top":
                            rob.put_wall(top=True)
                        elif wall_dir == "bottom":
                            rob.put_wall(bottom=True)
                        elif wall_dir == "left":
                            rob.put_wall(left=True)
                        elif wall_dir == "right":
                            rob.put_wall(right=True)

        # Робот начинает в верхнем левом углу
        rob.goto(start_r, start_c)

    def check_solution(self):
        if not rob.is_parking_point():
            return False
        return check_filled_cells(self.cells_to_fill)
