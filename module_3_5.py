def get_multiplied_digits(number):
    str_number = str(number)
    if number == 0:
        number += 1
    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return number


result = get_multiplied_digits(80600230)
print(result)
