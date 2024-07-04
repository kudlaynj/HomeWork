import math


def is_prime(func):
    def wraperr(*args, **kwargs):
        result = func(*args, **kwargs)
        n = 1
        if (math.factorial(n - 1) + 1) % n != 0:
            print('Составное')
        else:
            print('Простое')
            return result

    return wraperr


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
