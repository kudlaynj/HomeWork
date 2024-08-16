from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio


api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = InlineKeyboardMarkup()
button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb.add(button)
kb.add(button2)

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Информация')],
        [KeyboardButton(text='Рассчитать')],
    ], resize_keyboard=True)


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer(text='Выберите опцию:', reply_markup=kb)


@dp.callback_query_handler(text=['formulas'])
async def get_formulas(call):
    await call.message.answer(text='10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()


@dp.message_handler(commands=['start'])
async def starter(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=start_menu)


async def start_(message):
    await message.answer("Привет!", reply_markup=start_menu)


@dp.callback_query_handler(text='Информация')
async def inform(call):
    await call.message.answer(text='Информация о боте!', reply_markup=kb)
    await call.answer()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст:', reply_markup=kb)
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
