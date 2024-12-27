from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = '###'

bot = Bot(token=api)

dp = Dispatcher(bot, storage = MemoryStorage())


class User_srart(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text = ["Calories"])
async def set_age(message):
    await message.answer("Введите свой возраст:")
    await User_srart.age.set()

@dp.message_handler(state = User_srart.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await User_srart.growth.set()

@dp.message_handler(state = User_srart.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await User_srart.weight.set()

@dp.message_handler(state = User_srart.weight)
async def set_weight(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"]) - 161
    await message.answer(f"Ваша норма калорий - {calories} ккал")
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)