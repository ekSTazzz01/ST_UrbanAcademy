def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        count = 0
        if res < 2:
            return False
        for i in range(2, int(res ** 0.5) + 1):
            if res % i == 0:
                count = count + 1
        if count <= 0:
            print('Простое')
        else:
            print('Составное')
        return res
    return wrapper


@is_prime
def sum_three(*args):
    res = sum(args)
    return res


result = sum_three(3, 3, 3)
print(result)