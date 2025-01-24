# Импорт необходимых библиотек
import asyncio, sys
from distutils.command.check import check

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# Шапка работы
print ('Created by',sys.version)
print ('Домашнее задание по теме "Инлайн клавиатуры".')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Исходные данные настройкии бота
api = ''
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())
# Создание объекта класса ReplyKeyboardMarkup (он-лайн клавиатура) и задание параметра resize
kb = ReplyKeyboardMarkup()
ReplyKeyboardMarkup(resize_keyboard=True)
    # Данные для формирования кнопок он-лайн клавиатуры
dann_button_dict = {'inf':('Информация о боте','Бот ver 1.0'), 'ras': ('Расчет по Миффлину - Сан Жеору','Начинаем расчёт')}
    # Словарь кнопок он-лайн клавиатуры
button_dict = {}
        # Заполнение словаря кнопок
for i in dann_button_dict.keys():
    var_name = i
    button_dict[i] = KeyboardButton(text=dann_button_dict[i][0])
    # Размещение кнопок из словаря он-лайн клавиатуры button_dict в ряд
kb.row(*[i for i in button_dict.values()])
# Создание объекта класса InlineKeyboardMarkup(ин-лайн клавиатура) и задание параметра resize
kb_il = InlineKeyboardMarkup()
InlineKeyboardMarkup(resize_keyboard=True)
    # Данные для формирования кнопок ин-лайн клавиатуры
dann_button_dict_ik = {'clr': ('Рассчитать норму калорий', 'calories'),'frm': ('Формулы расчёта', 'formulas')}
    # Словарь кнопок ин-лайн клавиатуры
button_dict_ik = {}
        # Заполнение словаря кнопок
for i in dann_button_dict_ik.keys():
    var_name_ik = i
    button_dict_ik[i] = InlineKeyboardButton(text = dann_button_dict_ik[i][0], callback_data= dann_button_dict_ik[i][1])
    # Размещение кнопок из словаря ин-лайн клавиатуры button_dict_in
kb_il.add(*[i for i in button_dict_ik.values()])
# Описание класса состояний и классовых атрибутов
class User_State(StatesGroup):
    age = State()
    gender = State()
    growth = State()
    weight = State()
# Начало цепочки хендлеров, первый реагирует на команду /start, создаёт он-лайн клавиатуру
@dp.message_handler(commands=['start'])
async def start_ok(mess:Message):
    await mess.answer('Привет, начнем общение!', reply_markup=kb)
# Второй хендлер, вывод информации, реагирует на 'Информация о боте'
@dp.message_handler(text=['Информация о боте'])
async def inform(mess:Message):
    answ_butt = [i[1] for i in dann_button_dict.values() if i[0] == mess['text']]
    await mess.answer(*answ_butt)
# Третий хендлер, реагирующий на фразу 'Расчет по Миффлину - Сан Жеору', создаёт ин-лайн клавиатуру
@dp.message_handler(text = 'Расчет по Миффлину - Сан Жеору')
async def start_ik(mess: Message):
    answ_butt = [i[1] for i in dann_button_dict.values() if i[0] == mess['text']]
    await mess.answer(*answ_butt, reply_markup=kb_il)
# 4-й хендлер, реагирует на нажатие кнопки 'Формулы расчёта' (callback = formulas)
@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer('Формула Миффлина - Сан Жеора')
    await call.message.answer('для мужчин:')
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.message.answer('для женщин:')
    await call.message.answer('10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.')
    await call.answer()
# 4-й хендлер, реагирует на нажатие кнопки 'Рассчитать норму калорий' (callback = calories), запускает цепочку расчета,
# работу с состояниями, запрос age
@dp.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await User_State.age.set()
# 6-й хендлер, срабатывает на состояние User_State.age, запись данных age, установка состояния User_State.gender.
# Запрос gender
@dp.message_handler(state = User_State.age)
async def set_gender(mess, state: FSMContext):
    # Проверка ввода числа
    try:
        int(mess.text)
    except ValueError:
        await mess.reply('Введено не число, попробуйте еще раз.')
        return
    await state.update_data(age=mess.text)
    await mess.answer('Введите пол М или Ж:')
    await User_State.gender.set()
# 5-й хендлер, срабатывает на состояние User_State.gender, запись данных gender, установка состояния User_State.growth.
# Запрос growth
@dp.message_handler(state = User_State.gender)
async def set_growth(mess, state: FSMContext):
    # Проверка ввода М или Ж
    if mess.text.lower() not in ('м', 'ж'):
        await mess.reply('Ошибка, введите М или Ж')
        return
    await state.update_data(gender=mess.text)
    await mess.answer('Введите свой рост:')
    await User_State.growth.set()
# 6-й хендлер, срабатывает на состояние User_State.growth, запись данных growth, установка состояния User_State.weight.
# Запрос weight
@dp.message_handler(state = User_State.growth)
async def set_weight(mess, state: FSMContext):
    # Проверка ввода числа
    try:
        float(mess.text)
    except ValueError:
        await mess.reply('Введено не число, попробуйте еще раз.')
        return
    await state.update_data(growth=mess.text)
    await mess.answer('Введите свой вес:')
    await User_State.weight.set()
# 7-й хендлер, срабатывает на состояние User_State.weight, запись данных weight. Расчет rash_calories в зависимости от
# значения gender, вывод результата(rash_calories)
@dp.message_handler(state = User_State.weight)
async def send_calories(mess, state: FSMContext):
    # Проверка ввода числа
    try:
        float(mess.text)
    except ValueError:
        await mess.reply('Введено не число, попробуйте еще раз.')
        return
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