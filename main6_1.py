# Калькулятор 2.0
import math
import random

args0 = {'random'}
args1 = {'abs', 'acos', '!'}
args2 = {'+', '-', '*', '/', '**'}


def calc(opr, a=0.0, b=0.0):

    if opr in args0:
        return random.random()

    elif opr in args1:
        if opr == 'abs':
            return abs(a)

        elif opr == 'acos':
            if -1 <= a <= 1:
                return math.acos(a)
            else:
                print("Арккосинус не определён!")
                return None

        elif opr == '!':
            if a < 0:
                print("Невозможно найти факториал отрицательного числа!")
                return None
            else:
                return math.factorial(a)

    elif opr in args2:
        if opr == '+':
            return a + b

        elif opr == '-':
            return a - b

        elif opr == '*':
            return a * b

        elif opr == '/':
            if b == 0:
                print("Деление на 0 невозможно!")
                return None
            else:
                return a / b

        elif opr == '**':
            return a ** b


print("Введите необходимый символ операции:")
print("'+' - сложение")
print("'-' - вычитание")
print("'*' - умножение")
print("'/' - деление")
print("'**' - возведение в степень")
print("'abs' - модуль числа")
print("'random' - рандомное число")
print("'!' - факториал фисла")
print("'acos' - арккосинус числа\n")

operator = input("Ввод символа: ")
result = 0

if operator in args0:
    result = calc(operator)

elif operator in args1:
    firstNum = float(input("Введите число: "))
    result = calc(operator, firstNum)

elif operator in args2:
    firstNum = float(input("Введите первое число: "))
    secondNum = float(input("Введите второе число: "))
    result = calc(operator, firstNum, secondNum)

print("Результат: ", result)
