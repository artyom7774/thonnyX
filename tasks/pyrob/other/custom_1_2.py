#!/usr/bin/python3

import pyrob.core as rob
from tasks.pyrob import check_filled_cells, find_cells_to_be_filled
import random


class Task:
    CHECKS = 5

    def load_level(self, n):
        rows = random.randint(5, 20)
        cols = random.randint(5, 20)
        rob.set_field_size(rows, cols)

        # Старт и парковка
        start_r, start_c = 0, 0
        pr = random.randint(0, rows - 1)
        pc = random.randint(0, cols - 1)
        rob.set_parking_cell(pr, pc)
        rob.set_cell_type(pr, pc, rob.CELL_TO_BE_FILLED)
        self.cells_to_fill = find_cells_to_be_filled()

        # Все рёбра (соседние клетки)
        edges = []
        for r in range(rows):
            for c in range(cols):
                if r + 1 < rows:
                    edges.append(((r, c), (r + 1, c)))
                if c + 1 < cols:
                    edges.append(((r, c), (r, c + 1)))

        random.shuffle(edges)

        # DSU (система непересекающихся множеств)
        parent = {}
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        # Инициализация множеств
        for r in range(rows):
            for c in range(cols):
                parent[(r, c)] = (r, c)

        # Строим остовное дерево (оставляем проходы)
        mst = []
        for (a, b) in edges:
            if find(a) != find(b):
                union(a, b)
                mst.append((a, b))

        # Все остальные рёбра превращаем в стены
        for (a, b) in edges:
            if (a, b) not in mst and (b, a) not in mst:
                (r1, c1), (r2, c2) = a, b
                rob.goto(r1, c1)
                if r1 == r2:  # горизонтальная связь
                    if c1 < c2:
                        rob.put_wall(right=True)
                    else:
                        rob.put_wall(left=True)
                else:  # вертикальная связь
                    if r1 < r2:
                        rob.put_wall(bottom=True)
                    else:
                        rob.put_wall(top=True)

        # Робот начинает в верхнем левом углу
        rob.goto(start_r, start_c)

    def check_solution(self):
        if not rob.is_parking_point():
            return False
        return check_filled_cells(self.cells_to_fill)
