# Импорт необходимых библиотек
import sys
import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import Message
# Шапка работы
print ('Created by',sys.version)
print ('Домашнее задание по теме "Методы отправки сообщений"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Исходные данные настройкии бота
api = ''
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())
    # Словари ответов на команды и сообщения
answer_dict = {'Привет!': 'Доброе!', 'Ага': 'Наверное', 'Пока!': 'Пока!'}
command_dict = {'start': 'Привет! Я бот помогающий твоему здоровью', 'end': 'До свидания'}
# Хендлеры обработки сообщений в телеграмме
    # Вывод сообщений на введенные команды
@dp.message_handler(commands=[i for i in command_dict.keys()])
async def comm_mess(mess: Message):
    await mess.answer(command_dict[mess['text'][1:]])
    # Ответные сообщения на сообщения в боте
@dp.message_handler(text=[i for i in answer_dict.keys()])
async def answ_mess(mess: Message):
    await mess.answer(answer_dict[mess['text']])
    # Ответное сообщение на данные не учтенные в прошлых хендлерах
@dp.message_handler()
async def all_mess(mess: Message):
    await mess.answer('Введите команду /start, чтобы начать общение и /end, чтобы завершить')
# Запуск кода
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True )