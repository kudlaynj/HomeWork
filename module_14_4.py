from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import crud_functions

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Главное меню
start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Информация')],
        [KeyboardButton(text='Рассчитать')],
        [KeyboardButton(text='Купить')],
    ], resize_keyboard=True)

# Меню продуктов
produkt_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Кальций', callback_data='calcium')],
        [InlineKeyboardButton(text='Дегидрокварцетин', callback_data='dihydroquercetin')],
        [InlineKeyboardButton(text='Магний', callback_data='magnesium')],
        [InlineKeyboardButton(text='Мультифлора', callback_data='multiflora')],
    ])

# Панель администратора
admin_panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Продукт', callback_data='id')],
        [InlineKeyboardButton(text='Заголовок', callback_data='title')],
        [InlineKeyboardButton(text='Описание', callback_data='description')],
        [InlineKeyboardButton(text='Цена', callback_data='price')],
    ])


# Меню расчёта калорий
kb = InlineKeyboardMarkup()
button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb.add(button)
kb.add(button2)


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=start_menu)


@dp.message_handler(text=['Купить'])
async def get_buying_list(message: types.Message):
    # crud_functions.connection.close()
    await message.answer(text='Выберите продукт для покупки:', reply_markup=produkt_menu)


@dp.callback_query_handler(lambda call: call.data in ['calcium', 'dihydroquercetin', 'magnesium', 'multiflora'])
async def show_product_info(call: types.CallbackQuery):
    product_info = {
        'calcium': {
            'name': 'Кальций',
            'description': 'В качестве биологически активной добавки к пище - дополнительного '
                           'источника биодоступного кальция, '
            'витамина D3 и витамина К2. Входящий в состав кальций в биодоступной форме из аминокислотного '
            'хелатного комплекса с витаминами D3 и К2 для максимального усвоения способствуют: '
            'укреплению костной ткани, '
            'зубов, ногтей и волос, направляет кальций «прямо в цель» - без отложения в почках, суставах и сосудах; '
            'способствует снижению риска переломов костей и развития остеопороза.',
            'price': 100,
            'image': 'c:\\Users\\Admin\\PycharmProjects\\module_13\\kalcij_evalar.png'
        },
        'dihydroquercetin': {
            'name': 'Дегидрокварцетин',
            'description': 'Биологически активная добавка (БАД) к пище Дигидрокверцетин 100 мг –  это '
                           'биофлавоноид лиственницы '
            'сибирской – уникальное по совокупности своих полезных свойств вещество. Это более фармакологически'
            'чистая форма кверцетина, которая не является токсичной даже при сверхвысоких дозах. В ходе многочисленных '
            'научных исследований было доказано, что дигидрокверцетин способствует поддержанию в норме вязкости крови'
            ' и препятствует тромбообразованию. Дигидрокверцетин сохраняет здоровую эластичность, прочность сосудов и '
            'функциональную активность всей сердечно-сосудистой системы. ',
            'price': 200,
            'image': 'c:\\Users\\Admin\\PycharmProjects\\module_13\\dgkv.png'
        },
        'magnesium': {
            'name': 'Магний',
            'description': 'БАД к пище. Действие обусловлено свойствами компонентов, '
            'входящих в состав используемого продукта.'
            'В состав используемого продукта могут быть включены не все перечисленные ниже активные вещества.'
            'Магний необходим для обеспечения энергетических процессов, отвечает за передачу и скорость прохождения '
            'нервного импульса от головного мозга к периферическим нервным окончаниям и мышцам, участвует в процессах '
            'ослабления нервно-мышечного напряжения, поддерживая нормальную нервно-мышечную возбудимость, в том числе '
            'сократительную способность миокарда.',
            'price': 300,
            'image': 'c:\\Users\\Admin\\PycharmProjects\\module_13\\evalar-magnij.png'
        },
        'multiflora': {
            'name': 'Мультифлора',
            'description': 'Рекомендуется в качестве биологически активной добавки к пище – источника '
                           'пробиотических микроорганизмов. '
            'Синбиотик нового поколения (пробиотик+пребиотик). 7 видов живых бактерий в защитной двухслойной '
            'оболочке попадают в кишечник в неизменном виде и способствуют: восстановлению микрофлоры кишечника, '
            'в том числе после приема антибиотиков, укреплению иммунитета, улучшению пищеварения.',
            'price': 400,
            'image': 'c:\\Users\\Admin\\PycharmProjects\\module_13\\multiflora-evalar.png'
        }
    }

    product = product_info[call.data]

    # Кнопка "Купить" для каждого продукта
    buy_button = InlineKeyboardButton(text='Купить', callback_data=f'buy_{call.data}')
    buy_menu = InlineKeyboardMarkup().add(buy_button)

    # Отправка изображения продукта с его описанием и кнопкой "Купить"
    with open(product['image'], 'rb') as img:
        await bot.send_photo(
            chat_id=call.message.chat.id,
            photo=img,
            caption=(f"Название: {product['name']}\nОписание: {product['description']}\nЦена: {product['price']} руб."
                     ),
            reply_markup=buy_menu
        )


@dp.callback_query_handler(lambda call: call.data.startswith('buy_'))
async def handle_purchase(call: types.CallbackQuery):
    product_code = call.data.split('_')[1]

    product_names = {
        'calcium': 'Кальций',
        'dihydroquercetin': 'Дегидрокварцетин',
        'magnesium': 'Магний',
        'multiflora': 'Мультифлора'
    }

    product_name = product_names.get(product_code, 'Продукт')

    await call.message.answer(f"Вы успешно приобрели {product_name}!")
    await call.answer()


@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer(
        "Формула расчёта калорий:\n10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161"
    )
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост (в см):')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес (в кг):')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    weight = data['weight']
    growth = data['growth']
    age = data['age']

    # Формула расчета калорий (для женщин)
    result = (10 * weight) + (6.25 * growth) - (5 * age) - 161
    await message.answer(f'Ваша норма калорий: {result:.2f} ккал в день.')
    await state.finish()


@dp.message_handler(text='Информация')
async def inform(message: types.Message):
    await message.answer('Информация о боте!', reply_markup=start_menu)


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message: types.Message):
    await message.answer(text='Выберите опцию:', reply_markup=kb)


@dp.message_handler()
async def all_message(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
