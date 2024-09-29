class WordsFinder:    #Поиск слов

    def __init__(self, *file_name):
        self.file_names = [*file_name]
        self.file_name = file_name

    def get_all_words(self):           # получаем все слова в список
        self.all_words = {}
        words = []
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for p in punctuation:
                        if p in line:
                            line = line.replace(p, ' ')
                    sp_line = line.split(sep=' ')
                    words.append(sp_line)
            sort_list = [x for y in words for x in y]
            self.all_words[self.file_name] = sort_list
        return self.all_words

    def find(self, word):  # поиск
        self.word = word
        d = self.get_all_words()         # словарь - имя файла: [строки]
        dict_ = {}
        value = d.get(self.file_name)
        i = value.index(word.lower())
        dict_[(self.file_name)] = i + 1

        return dict_

    def count(self, word):  # cчет
        self.word = word
        dict_ = {}
        for index, w in self.get_all_words().items():
            words_count = w.count(word.lower())
            dict_[index] = words_count
            dict_[(self.file_name)] = words_count
        return dict_


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))





