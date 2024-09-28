class WordsFinder:    #Поиск слов

    file_names = {}

    def __init__(self, *name):
        self.name = name

    def get_all_words(self):           # получаем все слова
        all_words = {}
        key = ['file1.txt', 'file2.txt', 'file3.txt']
        value = ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7']
        with open('file1.txt', encoding='utf-8') as file:
            


        return {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}

#line = line.strip()