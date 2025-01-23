# Импорт необходимых библиотек
import asyncio, sys
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# Шапка работы
print ('Created by',sys.version)
print ('Домашнее задание по теме "Клавиатура кнопок"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Исходные данные настройкии бота
api = ''
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())
# Создание объекта класса ReplyKeyboardMarkup и задание его параметра
kb = ReplyKeyboardMarkup()
ReplyKeyboardMarkup(resize_keyboard=True)
# Данные для формирования кнопок
dann_button_dict = {'inf':('Информация','Бот ver 1.0'), 'ras': ('Расчет по Миффлину - Сан Жеору','Начинаем расчёт')}
# Словарь кнопок
button_dict = {}
    # Заполнение словаря кнопок
for i in dann_button_dict.keys():
    var_name = i
    button_dict[i] = KeyboardButton(text=dann_button_dict[i][0])
# Размещение кнопок из словаря в ряд
kb.row(*[i for i in button_dict.values()])
# Описание класса состояний и классовых атрибутов
class User_State(StatesGroup):
    age = State()
    gender = State()
    growth = State()
    weight = State()
# Начало цепочки хендлеров, первый реагирующий на команду /start
@dp.message_handler(commands=['start'])
async def start_kb(mess:Message):
    await mess.answer('Привет, начнем общение!', reply_markup=kb)
# Второй хендлер, вывод информации, реагирует на 'Информация'
@dp.message_handler(text=['Информация'])
async def inform(mess:Message):
    answ_butt = [i[1] for i in dann_button_dict.values() if i[0] == mess['text']]
    await mess.answer(*answ_butt)
# Третий хендлер, реагирующий на фразу 'Расчет по Миффлину - Сан Жеору', запускает работу с состояниями, запрос age
@dp.message_handler(text = 'Расчет по Миффлину - Сан Жеору')
async def set_age(mess: Message):
    answ_butt = [i[1] for i in dann_button_dict.values() if i[0] == mess['text']]
    await mess.answer(*answ_butt)
    await mess.answer('Введите свой возраст:')
    await User_State.age.set()
# 4-й хендлер, срабатывает на состояние User_State.age, запись данных age, установка состояния User_State.gender.
# Запрос gender
@dp.message_handler(state = User_State.age)
async def set_gender(mess, state: FSMContext):
    await state.update_data(age=mess.text)
    await mess.answer('Введите пол М или Ж:')
    await User_State.gender.set()
# 5-й хендлер, срабатывает на состояние User_State.gender, запись данных gender, установка состояния User_State.growth.
# Запрос growth
@dp.message_handler(state = User_State.gender)
async def set_growth(mess, state: FSMContext):
    await state.update_data(gender=mess.text)
    await mess.answer('Введите свой рост:')
    await User_State.growth.set()
# 6-й хендлер, срабатывает на состояние User_State.growth, запись данных growth, установка состояния User_State.weight.
# Запрос weight
@dp.message_handler(state = User_State.growth)
async def set_weight(mess, state: FSMContext):
    await state.update_data(growth=mess.text)
    await mess.answer('Введите свой вес:')
    await User_State.weight.set()
# 7-й хендлер, срабатывает на состояние User_State.weight, запись данных weight. Расчет rash_calories в зависимости от
# значения gender, вывод результата(rash_calories)
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