# Импорт необходимых библиотек
import sys
import asyncio
# Шапка работы
print ('Created by',sys.version)
print ('Домашнее задание по теме "Асинхронность на практике"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Исходные данные
dict_powerman = {'Портной': 1, 'Геракл': 4, 'Поддубный': 5}
# Асинхронная функция start_strongman (принимает name - имя, power - сила и ball - число шаров(по умолчанию - 5)
async def start_strongman(name, power, ball = 5):
    print(f'Силач {name} начал соревнование')
    for i in range(ball):
        await asyncio.sleep(power)
        print(f'Силач {name} поднял шар №{i + 1}')
    print(f'Силач {name} завершил соревнование!')
# Асинхронная функция start_tournament, принимает powerman - словарь участников и ball - число шаров(по умолчанию - 5)
async def start_tournament(powerman, ball = 5):
    dict_task = {}
    for i, j in powerman.items():
        dict_task[f'{i}'] = asyncio.create_task(start_strongman(i, j, ball))
    for i in dict_task.values():
        await i
# Запуск start_tournament со словарем участников dict_powerman
asyncio.run(start_tournament(dict_powerman))
