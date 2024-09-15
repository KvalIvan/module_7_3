class WordsFinder:
    def __init__(self, *args):
        self.args = args
        self.file_names = args

    def get_all_words(self):
        symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                all_words = {file_name: file.read().lower().split()}
                for symbol in symbols:
                    if symbol in all_words:
                        all_words = {file_name: file.read().lower().replace(symbol, '').split()}
        return all_words

    def find(self, word):
        find_word = {}
        number = 0
        for file_name, words in self.get_all_words().items():
            for f_word in words:
                number += 1
                if word.lower() in f_word:
                    find_word = {file_name: number}
                    break
        return find_word

    def count(self, word):
        count_word = {}
        number = 0
        for file_name, words in self.get_all_words().items():
            for c_word in words:
                if c_word == word.lower():
                    number += 1
            count_word = {file_name: number}
        return count_word


finder2 = WordsFinder('test.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
