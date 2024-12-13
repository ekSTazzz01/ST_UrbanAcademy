import io
from pprint import pprint

class WordsFinder:

    def __init__(self, *file_name):
        self.file_names = file_name


    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                text = file.read().lower()

                _punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for p in _punctuation:
                    if p in text:
                        text = text.replace(p, '')

                words = text.split()
                all_words[i] = words
        return all_words


    def find(self, word):
        word_index = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                word_index[name] = words.index(word.lower()) + 1
        return word_index


    def count(self, word):
        count_words = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                count_words[name] = words.count(word.lower())
        return count_words



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова

print(finder2.find('TEXT')) # 3 слово по счёту

print(finder2.count('teXT')) # 4 слова teXT в тексте всего