import os
import time

print('Текущая директория: ', os.getcwd())
# print(os.mkdir('folder'))
if os.path.exists('folder'):  # из метода path(пас) вызываем метод exists, который принимает путь и возвращает True, если путь существует и False, если такого пути нет
    os.chdir('folder')      #  - если  директория 'second' существует, то мы будем изменять с помощью метода chdir на 'second'
else:
    os.mkdir('folder')   #  если директории нет, то мы ее будем создавать
    os.chdir('folder')
# print(os.chdir('folder'))
# os.makedirs(r'folder1\folder2')
print('Текущая директория: ', os.getcwd())

rootDir = '.'

for dirName, subdirList, fileList in os.walk(rootDir):
    print('Найден каталог: %s' % dirName)
    for fname in fileList:
        print(r'\t%s' % fname)

seconds = time.time()

for root, dirs, files in os.walk(rootDir):
  for file in files:
    base_dir = r'C:\Users\nikit\PycharmProjects\pythonProject7\folder'
    full_path = os.path.join(base_dir, 'folder')  # полный путь к файлу
    filetime = os.path.getmtime(file)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    file_size = os.path.getsize(file)
    parent_dir = os.path.dirname(full_path)

    print(f'Обнаружен файл: {file}, Путь: {full_path}, Размер: {file_size} байт, Время изменения: {formatted_time}, '
      f'Родительская директория: {parent_dir}')


