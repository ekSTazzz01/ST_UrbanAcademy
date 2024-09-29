first = int(input('введите первое целое число:'))
second = int(input('введите второе целое число:'))
third = int(input('введите третье целое число:'))


if first == second == third:
    print('3')

elif first == second or second == third or first == third:
    print('2')

elif first != second != third:
    print('0')


