import random


class Task:
    RTEST = 100
    CTEST = 3

    @staticmethod
    def ctest():
        return ["1\n3", "4\n2", "3\n7"]

    @staticmethod
    def rtest():
        return [f"{random.randint(1, 20)}\n{random.randint(1, 20)}" for _ in range(Task.RTEST)]


Task.INFORMATION = """
  Дана масса в граммах. Переведите её в килограммы  
и граммы.
(Упр 3.3 страница 140)
"""

Task.FUNCTION = """
x = int(input())
a = x // 1000
b = x % 1000

print(a,b)
"""
