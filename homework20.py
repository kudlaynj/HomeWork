def f1(x):
    return x*x


def f2(x):
    return x % 2


number = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

res = map(f1, filter(f2, number))
print(list(res))
