def print_params(a=1, b="строка", c=True):
    print(a, b, c)


print_params('Лягушка', c='да')
print_params()
print_params(*[5, 6, 7])
values_list = ["Ло", 113, 15.5]
values_dict = {'a': 73, 'b': "регион", 'c': False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ["qwerty", 90]
print_params(*values_list_2, 33)