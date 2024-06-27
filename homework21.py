print('Задача 1: Фабрика функций')


def f1(x, y):
    return x + y


def f2(x, y):
    return x - y


def f3(x, y):
    return x * y


fun = f3(3, 2)
fun_1 = f2(4.0, 2)

print(fun)
print(fun_1)

try:
    x = 10
    x / 0
except ZeroDivisionError:
    print('Error: Division by zero')

print('Задача 2: Лямбда')

multiply = lambda x, y: x * y
print(multiply(8, 2))


def multiply_def(x, y):
    return x * y


print(multiply_def(8, 2))

print('Задача 3: Вызываемые Объекты')


class Rect:
    def __init__(self, a, b):
        self.a = 0
        self.b = 0

    def __call__(self, a, b):
        return a * b


repeat_five = Rect(2, 4)
print(repeat_five(2, 4))
