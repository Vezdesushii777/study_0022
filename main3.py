# Калькулятор
import math
import random

x = input("Введите необходимый символ операции: +, -, *, /, **, abs, random, !, acos\n")

if x == "+":
    a = float(input("Введите первое слагаемое: "))
    b = float(input("Введите второе слагаемое: "))
    print("Сумма:", a + b)

elif x == "-":
    a = float(input("Введите уменьшаемое: "))
    b = float(input("Введите вычитаемое: "))
    print("Разность:", a - b)

elif x == "*":
    a = float(input("Введите первый множитель: "))
    b = float(input("Введите второй множитель: "))
    print("Произведение:", a * b)

elif x == "/":
    a = float(input("Введите делимое: "))
    b = float(input("Введите делитель: "))
    if b == 0:
        print("Деление на 0 невозможно!")
    else:
        print("Частное:", a / b)

elif x == "**":
    a = float(input("Введите число, которое необходимо возвести в степень: "))
    b = float(input("Введите степень: "))
    print("Возведение в степень:", a ** b)

elif x == "abs":
    a = float(input("Введите число, модуль которого необходимо найти: "))
    print("Модуль числа:", abs(a))

elif x == "random":
    print("Рандомное число: ", random.random())

elif x == "!":
    a = int(input("Введите число, факториал которого необходимо найти: "))
    if a < 0:
        print("Невозможно найти факториал отрицательного числа!")
    else:
        print("Факториал:", math.factorial(a))

elif x == "acos":
    a = float(input("Введите число, арккосинус которого необходимо найти: "))
    if -1 <= a <= 1:
        print("Арккосинус:", math.acos(a))
    else:
        print("Арккосинус не определён!")
