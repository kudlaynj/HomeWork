def test(*params):
    print(params)

test(11, 22, 33, 44, 55)


def test_2(n, *args, txt="Сумма"):
    s = 0
    for i in range(len(args)):
        s += args[i] ** n
        print(txt + ":", s)


test_2(4, 2,4,6,8)

