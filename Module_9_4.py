from random import choice

# Lambda-функция:

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)

# Замыкание функция:

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open('example.txt', 'w', encoding='utf-8') as file:
            for i in data_set:
                file.write(str(i) + '\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Замыкание класс:

class MysticBall:
    def __init__(self, *words: tuple):
        self.words = words

    def __call__(self):
        wc = choice(self.words)
        return wc

first_ball = MysticBall('Зачет', 'Незачет', 'Оценка')
print(first_ball())
print(first_ball())
print(first_ball())