import random
import math

i = int(1)


class Operation:
    tip = ""

    def display_info(self):
        print("Операция :", self.tip)


operation1 = Operation()
operation1.tip = "Сумма"
operation2 = Operation()
operation2.tip = "Разность"
operation3 = Operation()
operation3.tip = "Произведение"
operation4 = Operation()
operation4.tip = "Деление"
operation5 = Operation()
operation5.tip = "Возведение в степень"
operation6 = Operation()
operation6.tip = "Факториал"
operation7 = Operation()
operation7.tip = "Случайное число"
operation8 = Operation()
operation8.tip = "Арккосинус"
operation9 = Operation()
operation9.tip = "Модуль числа"
while i < 2:
    print("+, -, *, /, ^, !, rand, acos, mod")
    oper = input("Введите операцию ")
    if oper == '+':
        operation1.display_info()
        x = float(input("Введите первое число "))
        y = float(input("Введите второе число "))
        print(x + y)
    elif oper == '-':
        operation2.display_info()
        x = float(input("Введите первое число "))
        y = float(input("Введите второе число "))
        print(x - y)
    elif oper == '*':
        operation3.display_info()
        x = float(input("Введите первое число "))
        y = float(input("Введите второе число "))
        print(x * y)
    elif oper == '/':
        operation4.display_info()
        x = float(input("Введите первое число "))
        y = float(input("Введите второе число "))
        print(x / y)
    elif oper == '^':
        operation5.display_info()
        x = float(input("Введите число "))
        y = float(input("Введите степень числа "))
        print(pow(x, y))
    elif oper == '!':
        operation6.display_info()
        a = int(input("Введите число, для которого нужно найти факториал "))
        print(math.factorial(a))
    elif oper == 'rand':
        operation7 .display_info()
        print(random.random())
    elif oper == 'acos':
        operation8 .display_info()
        x = float(input("Введите число от -1 до 1 "))
        print("ответ в радианах ", math.acos(x))
    elif oper == 'mod':
        operation9.display_info()
        x = float(input("Введите число "))
        x = abs(x)
        print(x)
    else:
        print("Ошибка")
input()+