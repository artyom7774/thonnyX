import random


class Task:
    RTEST = 100
    CTEST = 3

    @staticmethod
    def ctest():
        return ["15", "44", "31"]

    @staticmethod
    def rtest():
        return [f"{random.randint(10, 99)}" for _ in range(Task.RTEST)]


Task.INFORMATION = """
 Задано положительное двузначное число. Найдите раз
ность между количеством десятков и единиц.
(Упр 3.2 страница 140)
"""

Task.FUNCTION = """
x = int(input())
a = x // 10
b = x % 10
d = a-b

print(d)
"""
