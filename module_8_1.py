def add_everything_up(a, b):
    try:
        res = a + b
        return round(res, 3)
    except TypeError:
        a1 = str(a)
        b1 = str(b)
        return a1 + b1


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
