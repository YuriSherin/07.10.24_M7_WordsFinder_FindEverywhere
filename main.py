class WordsFinder:
    file_names = None
    """Класс при создании принимает неограниченное количество имен файлов
    и сохраняет их в атрибуте file_names в виде списка"""
    def __init__(self,*f_names):
        """Конструктор класса"""
        self.file_names = []
        for fn in f_names:
            self.file_names.append(fn)

    def get_all_words(self) -> dict:
        """Метод возвращает словарь следующего вида:
        {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4']},
        где ключ - имя файла, значение - список слов, содержащиеся в этом файле"""
        all_words = {}
        exclude = set([',', '.', '=', '!', '?', ';', ':', ' - ', '...'])       # используем `set()` для скорости

        for fn in self.file_names:
            words = []
            try:
                with open(fn, 'r', encoding='utf8') as file:
                    for ln in file:
                        line = ln.lower()
                        s = ''.join(ch for ch in line if ch not in exclude)
                        words += s.split()
            except ValueError as e:
                print(f'При попытке прочтении файла {fn} ошибка: {e}')
            all_words[fn] = words

        return all_words

    def find(self, word: str) -> dict:
        """Метод возвращает словарь, где ключ - имя файла,
        значение - позиция первого вхождения искомого слова в список слов этого файла,
        если слово не найдено в списке - значение равно -1"""
        res = {}
        for key, item in self.get_all_words().items():
            i = 0
            res[key] = -1
            for w in item:
                if w == word.lower():
                    res[key] = i + 1
                    break
                i += 1
        return res


    def count(self, word: str) -> dict:
        """Метод возвращает словарь, где ключ - имя файла,
        значение - количество вхождений искомого слова в список слов этого файла"""
        res = {}
        for key, item in self.get_all_words().items():
            res[key] = item.count(word.lower())
        return res

if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt', 'poem.txt')
    print('Вывод всех слов из словаря: ', finder2.get_all_words())
    print('Поиск слова TEXT: ', finder2.find('TEXT'))
    print('Количество слов teXT: ', finder2.count('teXT'))
    print('Поиск слова жДи: ', finder2.find('жДи'))
    print('Количество слов верНусь: ', finder2.count('верНусь'))
