from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio


api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup()
button = KeyboardButton(text='Информация')
button2 = KeyboardButton(text='Рассчитать')
kb.add(button)
kb.add(button2)

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Информация')],
        [KeyboardButton(text='Рассчитать')],
    ],resize_keyboard=True)


@dp.message_handler(commands=['start'])
async def starter(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=start_menu)


async def start_(message):
    await message.answer("Привет!", reply_markup=start_menu)


@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer('Информация о боте!', reply_markup=kb)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text=['Рассчитать'])
async def set_age(message: types.Message):
    await message.answer('Введите свой возраст:', reply_markup=kb)
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_colories(message: types.Message, state: FSMContext):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    weight = data['weight']
    growth = data['growth']
    age = data['age']
    result = ((10.0 * weight) + 6.25 * growth - (5.0 * age) - 161.0)
    await message.answer(f'Ваша норма калорий: {result:.2f}')
    await state.finish()


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    print("Start message")
    await message.answer("Привет! Я бот помогающий твоему здоровью.")


@dp.message_handler()
async def all_message(message: types.Message):
    print("Введите команду /start, чтобы начать общение.")
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
