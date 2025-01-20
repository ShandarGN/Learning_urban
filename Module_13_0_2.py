from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = '8152434193:AAF1hKtNsBIRX50ZU3XlkLS6cVsNX8Sydl8'
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

command_dict = {'start': 'Привет! Я бот помогающий твоему здоровью', 'end': 'До свидания'}

@dp.message_handler(commands=['start', 'end'])
async def start_mes(mess):
    print(command_dict[mess['text'][1:]])

@dp.message_handler()
async def all_mess(mess):
    print('Введите команду /start, чтобы начать общение и /end, чтобы завершить')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True )