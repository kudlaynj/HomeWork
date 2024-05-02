def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = ['home', 786, [6, 7, 8]]
values_dict = {'a': 2, 'b': 3, 'c': 4}
values_list_2 = [6, 'port']
print_params()
print_params(a = 48, b = 56, c = 34)
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)

