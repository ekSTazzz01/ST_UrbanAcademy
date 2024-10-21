call = 0

def count_call():
    global call


count_call()


def string_info(string):
    global call
    call = call + 1


    w_len = len(string)
    w_upper = string.upper()
    w_lower = string.lower()
    return w_len, w_upper, w_lower


def is_contains(string, list_to_search):
    global call
    call = call + 1


    list_lower = [i.lower() for i in list_to_search]
    w_lower = string.lower()
    if w_lower in list_lower:
        print('True')
    else:
        print('False')
    return


print(string_info('Университет'))
print(string_info('Python'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(call)


