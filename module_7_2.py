def custom_write(file_name, strings):
    file_name = 'list_strings.txt'

    elem = {}
    n = 0

    for i in info:
        file = open(file_name, 'a', encoding='utf-8')
        text_tell = file.tell()
        n += 1
        file.write(f'{i}\n')
        file.close()
        elem.update({(n, text_tell): i})
    return elem


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('list_strings.txt', info)
for elem in result.items():
  print(elem)