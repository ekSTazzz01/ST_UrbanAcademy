def print_params(a =1, b = 'string', c = True):
    print (a, b, c)

values_list = [8, 'urban', False]
values_dict = {'a' : 3, 'b' : 'academy', 'c' : True}
values_list_2 = [64.12, 'urban']


print_params(2, 8, c = True )
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 9)