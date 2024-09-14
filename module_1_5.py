immutable_var = 1, 2, 3, True, 'Urban'
print(immutable_var)
# immutable_var[3] = 250 # изменение невозможно,т.к. кортеж не поддерживает обращение по элементам
print(immutable_var)
mutable_list = ['Urban', 'Academy', 'Student']
print(mutable_list)
mutable_list[1] = 'University'
print(mutable_list)
mutable_list[0] = 500
print(mutable_list)