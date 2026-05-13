import random


class Task:
    RTEST = 100
    CTEST = 3

    @staticmethod
    def ctest():
        return ["19", "41", "33"]

    @staticmethod
    def rtest():
        return [f"{random.randint(10, 99)}" for _ in range(Task.RTEST)]


Task.INFORMATION = """
 Задано положительное двузначное число. Найдите среднее 
арифметическое цифр числа.
(Упр 3.1 страница 140)
"""

Task.FUNCTION = """
x = int(input())
a = x // 10
b = x % 10
d = (a + b) / 2

print(d)
"""
