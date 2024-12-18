def personal_sum(numbers):
    incorrect_date = 0
    result = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_date += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
    return result, incorrect_date



def calculate_average(numbers):
    try:
        total, incorrect_date  = personal_sum(numbers)
        return total/(len(numbers) - incorrect_date)
    except ZeroDivisionError:
        return 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных')



print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать