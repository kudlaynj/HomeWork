def test():
    a = 12
    b = 25
    print(a, b)


def test2(n):
    if n == 0:
        return 0
    else:
        return n + test2(n - 1)


test()

print(test2(7))
