import random


class Task:
    RTEST = 100
    CTEST = 3

    @staticmethod
    def ctest():
        return ["1\n3", "4\n2", "3\n7"]

    @staticmethod
    def rtest():
        return [f"{random.randint(1, 200000)}\n{random.randint(1, 20)}" for _ in range(Task.RTEST)]


Task.INFORMATION = """
   Площадь участка измеряется в арах. Выразите эту площадь
   в квадратных километрах (найдите их полное количество).
(Упр 3.4 страница 140)
"""

Task.FUNCTION = """
x = int(input())
a = x // 10000
b = x % 10000

print(a)
"""
