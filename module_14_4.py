from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio

from crud_functions import *


api = '###'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# кнопки в самом начале
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text="Расчитать")
button1 = KeyboardButton(text="Начало")
button2 = KeyboardButton(text="Купить")
kb.add(button, button1)
kb.add(button2)


# меню при нажатии кнопки расчитать
menu_calculation = InlineKeyboardMarkup()
inline_button_calc_1 = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data='calories')
inline_button_calc_2 = InlineKeyboardButton(text="Формула расчёта", callback_data='formulas')
menu_calculation.add(inline_button_calc_1, inline_button_calc_2)


# меню при нажатии кнопки купить
menu_buy = InlineKeyboardMarkup()
inline_button_buy_1 = InlineKeyboardButton(text="Омега 3", callback_data="product_buying")
inline_button_buy_2 = InlineKeyboardButton(text="Витамин D3", callback_data="product_buying")
inline_button_buy_3 = InlineKeyboardButton(text="Магний + B6", callback_data="product_buying")
inline_button_buy_4 = InlineKeyboardButton(text="Триптофан", callback_data="product_buying")
menu_buy.add(inline_button_buy_1, inline_button_buy_2, inline_button_buy_3, inline_button_buy_4)


class User_start(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# приветствие вначале
@dp.message_handler(commands="start")
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью!", reply_markup=kb)


# дальнейшие действия при нажатии кнопки расчитать
@dp.message_handler(text="Расчитать")
async def menu_start(message):
    await message.answer("Выберите опцию:", reply_markup=menu_calculation)


@dp.callback_query_handler(text="calories")
async def calories(call):
    await call.message.answer("Введите свой возраст:")
    await User_start.age.set()
    await call.answer()


@dp.message_handler(state=User_start.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await User_start.growth.set()


@dp.message_handler(state=User_start.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await User_start.weight.set()


@dp.message_handler(state=User_start.weight)
async def set_weight(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories_form = 10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"]) - 161
    await message.answer(f"Ваша норма калорий - {calories_form} ккал")
    await state.finish()


@dp.callback_query_handler(text="formulas")
async def calories(call):
    await call.message.answer("10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161")
    await call.answer()


# дальнейшие действия при нажатии кнопки купить
@dp.message_handler(text="Купить")
async def get_buying_list(message):
    for i in range(1, 5):
        with open(f'{i}.jpg', 'rb') as img:
            product = get_all_products(i)
            await message.answer_photo(img, f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}')
    await message.answer("Выберите продукт для покупки:", reply_markup=menu_buy)


@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
