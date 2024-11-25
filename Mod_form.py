# Шапка работы
import sys
print ('Created by',sys.version)
print ('Домашнее задание по теме "Форматирование строк"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Функция определения окончания
def ends(num):
    if num % 10 == 1:
        return ''
    elif num % 10 > 1 and num % 10 < 5:
        return 'а'
    else:
        return 'ов'
# Исходные данные
    # Названия команд
name_1 = 'Мастера кода'
name_2 = 'Волшебники данных'
    # Количество решённых задач по командам:
score_1 = 40
score_2 = 42
    # Число участников команд
team1_num = 5
team2_num = 6
    # Количество решённых задач по командам:
score_1 = 40
score_2 = 42
    # Время за которое команды решили задачи
team1_time = 18015.2
team2_time = 19125.8

# Использование %:
    # Словарь имен переменных и значений
dict_team = {'team1_num': 5, 'team2_num': 6, 'okon1': ends(team1_num), 'okon2': ends(team2_num)}
    # Вывод данных
print('В команде %s участник%s: %s' % (name_1, dict_team['okon1'], team1_num))
print('В команде %s участник%s: %s' % (name_2, dict_team['okon2'], team2_num))
print('Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s!' % dict_team)

# Использование format():
    # Вывод данных
print('Команда {} решила задач: {}'.format(name_1, score_1))
print('Команда {} решила задач: {}'.format(name_2, score_2))
print('{frst} решили задачи за: {scnd} сек.'.format(frst=name_1, scnd=team1_time))
print('{frst} решили задачи за: {scnd} сек.'.format(frst=name_2, scnd=team2_time))

# Использование f-строк:
    # Функция определения исход соревнования и подсчета итоговых данных
def result(name01, name02, score01, score02, team01_time, team02_time):
    pref = 'победа команды '
    # Блок подсчета итоговых данных
    tasks_total = score01 + score02
    time_avg = round((team01_time + team02_time)/(score01 + score02),2)
    # Блок определения победителя
    if score01 > score02:
        return pref + name01, tasks_total, time_avg
    elif score02 > score01:
        return pref + name02, tasks_total, time_avg
    else:
        if team01_time < team02_time:
            return pref + name01, tasks_total, time_avg
        elif team02_time < team01_time:
            return pref + name02, tasks_total, time_avg
        else:
            return 'ничья', tasks_total, time_avg
itog = result(name_1, name_2, score_1, score_2, team1_time, team2_time)
    # Вывод данных
print(f'Результат битвы: {itog[0]}, всего решено задач: {itog[1]}, среднее время решения: {itog[2]} секунд')

