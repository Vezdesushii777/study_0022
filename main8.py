# Калькулятор 3.0
import math
import random

args0 = {'random'}
args1 = {'abs', 'acos', '!'}
args2 = {'+', '-', '*', '/', '**'}


class Calculator:
    a = 0.0
    b = 0.0
    opr = ""

    def count(self):

        if self.opr in args0:
            return random.random()

        elif self.opr in args1:
            if self.opr == 'abs':
                return abs(self.a)

            elif self.opr == 'acos':
                if -1 <= self.a <= 1:
                    return math.acos(self.a)
                else:
                    print("Арккосинус не определён!")
                    return None

            elif self.opr == '!':
                if self.a < 0:
                    print("Невозможно найти факториал отрицательного числа!")
                    return None
                else:
                    return math.factorial(self.a)

        elif self.opr in args2:
            if self.opr == '+':
                return self.a + self.b

            elif self.opr == '-':
                return self.a - self.b

            elif self.opr == '*':
                return self.a * self.b

            elif self.opr == '/':
                if self.b == 0:
                    print("Деление на 0 невозможно!")
                    return None
                else:
                    return self.a / self.b

            elif self.opr == '**':
                return self.a ** self.b


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


result = 0
calc = Calculator()
calc.opr = input("Ввод символа: ")

if calc.opr in args0:
    result = calc.count()

elif calc.opr in args1:
    calc.a = float(input("Введите число: "))
    result = calc.count()

elif calc.opr in args2:
    calc.a = float(input("Введите первое число: "))
    calc.b = float(input("Введите второе число: "))
    result = calc.count()

print("Результат: ", result)
