# Импорт необходимых библиотек
import asyncio, re, sys
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
# Шапка работы
print ('Created by',sys.version)
print ('Домашнее задание по теме "Машина состояний"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Исходные данные настройкии бота
api = ''
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())
# Описание класса состояний и классовых атрибутов
class User_State(StatesGroup):
    age = State()
    gender = State()
    growth = State()
    weight = State()
# Начало цепочки хендлеров, первый хендлер, реагирующий на слово 'калории' без учета регистра, запрос age
@dp.message_handler(regexp=re.compile('калории', flags=re.IGNORECASE))
async def set_age(mess: Message):
    await mess.answer('Введите свой возраст:')
    await User_State.age.set()
# 2-й хендлер, срабатывает на состояние User_State.age, запись данных age, установка состояния User_State.gender.
# Запрос gender
@dp.message_handler(state = User_State.age)
async def set_gender(mess, state: FSMContext):
    await state.update_data(age=mess.text)
    await mess.answer('Введите пол М или Ж:')
    await User_State.gender.set()
# 3-й хендлер, срабатывает на состояние User_State.gender, запись данных gender, установка состояния User_State.growth.
# Запрос growth
@dp.message_handler(state = User_State.gender)
async def set_growth(mess, state: FSMContext):
    await state.update_data(gender=mess.text)
    await mess.answer('Введите свой рост:')
    await User_State.growth.set()
# 4-й хендлер, срабатывает на состояние User_State.growth, запись данных growth, установка состояния User_State.weight.
# Запрос weight
@dp.message_handler(state = User_State.growth)
async def set_weight(mess, state: FSMContext):
    await state.update_data(growth=mess.text)
    await mess.answer('Введите свой вес:')
    await User_State.weight.set()
# 5-й хендлер, срабатывает на состояние User_State.weight, запись данных weight. Расчет rash_calories в зависимости от
# значения age, вывод результата(rash_calories)
@dp.message_handler(state = User_State.weight)
async def send_calories(mess, state: FSMContext):
    await state.update_data(weight=mess.text)
    data = await state.get_data()
    if data['gender'].lower() == 'м':
        rash_calories = (float(data['age'])* 5 + 5) + (float(data['growth'])*6.25) + (float(data['weight'])*10)
    elif data['gender'].lower() == 'ж':
        rash_calories = (float(data['age']) * 5 - 161) + (float(data['growth']) * 6.25) + (float(data['weight']) * 10)
    await mess.answer(f'Вам нужно {rash_calories} калорий')
    await state.finish()
# Запуск кода
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True )