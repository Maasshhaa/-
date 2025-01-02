from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio

api = '###'

bot = Bot(token=api)

dp = Dispatcher(bot, storage=MemoryStorage())

menu = InlineKeyboardMarkup()
inline_button = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data='calories')
inline_button1 = InlineKeyboardButton(text="Формула расчёта", callback_data='formulas')
menu.add(inline_button, inline_button1)
# menu.add(inline_button1)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text="Расчитать")
button1 = KeyboardButton(text="Начало")
kb.add(button)
kb.add(button1)


class User_start(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands="start")
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью!", reply_markup=kb)


@dp.message_handler(text="Расчитать")
async def manu_start(message):
    await message.answer("Выберите опцию:", reply_markup=menu)


@dp.callback_query_handler(text="calories")
async def calories(call):
    await call.message.answer("Введите свой возраст:")
    await User_start.age.set()
    await call.answer()
# async def set_age(message):
#     await message.answer("Введите свой возраст:", reply_markup=kb)
#     await User_srart.age.set()


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


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
