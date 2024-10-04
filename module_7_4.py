from pprint import pprint

def custom_write(file_name: str, strings: list):
    strings_positions = {}
    line_number = 1
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        line_byte = file.tell()
        file.write(f'{string}\n')
        strings_positions[(line_number, line_byte)] = string
        line_number += 1
        pprint(file.tell())
    file.close()
    return strings_positions

if __name__ == '__main__':
    info = [                            'Хакатон "Печенька" ',
'    В ознаменование празднования "Дня Печеньки" между специалистами из разных областей разработки программного',
'обеспечения на платформе Codenrock был проведен Хакатон. На соревновании собенно отличились команды: "Мастера',
'кода" и "Волшебники данных". Состязание длилось 18015.2 секунд.']  # запись текста в файл построчно

    result = custom_write('article.txt', info)
    for elem in result.items():
        print(elem)     # вывод текста в консоль


team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'
time = 18015.2
team1_num = 5
team2_num = 6
quantity1 = (input('Сколько задач решила команда Мастера кода? '))   # ввод пользовательского текста
quantity2 = (input('Сколько задач решила команда Волшебники данных? '))  # ввод пользовательского текста
sum_ = int(quantity1) + int(quantity2)

print("В команде %s участников %s, в команде %s участников %s. Итого сегодня в командах участников - %s и %s !"\
         % (team1_name, team1_num, team2_name, team2_num, team1_num, team2_num))     #вывод строки в консоль


def about_tasks(team_name):  # о задачах
    if team_name == team1_name:
        quantity = quantity1
    else:   quantity = quantity2

    print("За {} секунд команда {} решила {} задач!".format(time, team_name, quantity))
about_tasks(team1_name)                   #вывод строки в консоль
about_tasks(team2_name)                   #вывод строки в консоль


print(f'Команды решили {quantity1} и {quantity2} задач. Всего сегодня было решeно {sum_} задач.')  #вывод строки в консоль

def score_(team_name):
    if team_name == team1_name:
        quantity = float(quantity1)
    else: quantity = float(quantity2)
    if team_name == team1_name:
        team_num = team1_num
    else: team_num = team2_num
    average_time = time/quantity           # среднее время решения одной задачи
    average_quantity = quantity/team_num          # среднее количество задач, решенных одним участником
    print(f'Командой {team_name} в среднем было затрачено по {average_time} секунд на решение одной задачи.'
          f'Среднее количество задач, решенных одним участником, составило {average_quantity}')
    return average_quantity

def victory_():
    result1 = score_(team1_name)
    result2 = score_(team2_name)
    if result1 > result2:
        print(f'Результат битвы: победа команды {team1_name}! Программисты покорили судей неординарным подходом.'
        'Навыки работы в команде и благоприятная атмосфера помогли обеим командам преодолеть трудности.'
        'Чаепитие с ароматным печеньем завершило это мероприятие.')
    if result1 < result2:
        print(f'Результат битвы: победа команды {team2_name}! Программисты покорили судей неординарным подходом.'
        'Навыки работы в команде и благоприятная атмосфера помогли обеим командам преодолеть трудности.'
        'Чаепитие с ароматным печеньем завершило это мероприятие.')
    elif result1 == result2:
        print(f'Результат битвы: ничья! Программисты покорили судей неординарным подходом.'        
        'Навыки работы в команде и благоприятная атмосфера помогли обеим командам преодолеть трудности.'
        'Чаепитие с ароматным печеньем завершило это мероприятие.')

victory_()     #вывод строк в консоль

with open('article.txt', 'a', encoding='utf-8') as file:   # запись текста в файл
    infos = file.write('\n'.join(iter(input, '')))    # необходимо скопировать строки, выведенные в консоль и ввести их
    # как пользовательский текст + Enter + Enter

from textwrap import TextWrapper

class DocumentWrapper(TextWrapper):

    def wrap(self, text):
        split_text = text.split('\n')
        lines = [line for par in split_text for line in TextWrapper.wrap(self, par)]
        return lines

with open('article.txt', "r", encoding="utf-8") as file:
    for lines in file:
        print((file.seek(0)))
        textwrap = file.read()
        d = DocumentWrapper(width=65)
        print(d.fill(textwrap))
