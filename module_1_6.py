my_dict = {'Stas': 1983, 'John': 1984, 'Yana': 1984}
print(my_dict)
print(my_dict['Stas'])
print(my_dict.get ('Vika'))
my_dict.update ({'Natasha': 1962, 'Vasya': 1961})
new_value = my_dict.pop('Yana')
print(new_value)
print(my_dict)

my_set = {9, 8, 5, 9, 3, 5, 'Stas'}
print(my_set)
my_set.update((3.14, 'Yana'))
my_set.remove(3)
print(my_set)
