import asyncio

dict_powerman = {'Портной': 1, 'Геракл': 4, 'Поддубный': 5}

async def start_strongman(name, power, ball = 5):
    print(f'Силач {name} начал соревнование')
    for i in range(ball):
        await asyncio.sleep(power)
        print(f'Силач {name} поднял шар №{i + 1}')
    print(f'Силач {name} завершил соревнование!')

async def start_tournament(powerman, ball = 5):
    dict_task = {}
    for i, j in powerman.items():
        dict_task[f'{i}'] = asyncio.create_task(start_strongman(i, j, ball))
    for i in dict_task.values():
        await i

asyncio.run(start_tournament(dict_powerman))

