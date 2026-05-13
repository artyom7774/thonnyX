import random


class Task:
    RTEST = 100
    CTEST = 3

    @staticmethod
    def ctest():
        return ["1024", "4000", "300"]

    @staticmethod
    def rtest():
        return [f"{random.randint(1, 21000)}}" for _ in range(Task.RTEST)]


Task.INFORMATION = """
  Размер файла задан в килобайтах. Переведите его в мега
байты и килобайты.
(Упр 3.5 страница 140)
"""

Task.FUNCTION = """
x = int(input())
a = x // 1024
b = x % 1024

print(a,b)
"""
