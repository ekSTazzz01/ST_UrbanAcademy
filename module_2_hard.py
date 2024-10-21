def set_password(Num):
    for i in range(1, 21):
        for j in range(i + 1, Num):
            if Num % (i + j) == 0:
                print(f'{i} {j}')
    return


Num = int(input('Введите число от 3 до 20: '))

set_password(Num)
