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
Найти значение выражения x ** 2 / (y + 1) при заданных x, y
(Упр 1.1 страница 111)
"""

Task.FUNCTION = """
x = int(input())
y = int(input())

print(x ** 2 / (y + 1))
"""
