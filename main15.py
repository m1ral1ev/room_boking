import logging
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# TOKEN = 2056044585:AAEbna31vSlu3pXQ0gofUd4V__sMCPq-F5k

bot = Bot(token='2056044585:AAEbna31vSlu3pXQ0gofUd4V__sMCPq-F5k')

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class Form(StatesGroup):
    contact = State()
    car = State()
    level = State()
    color = State()
    just = State()
    pay_via = State()
    info = State()

# main menu


@dp.message_handler(commands="start")
async def start_cmd(message: types.Message):
    if message.from_user.id == 1187125731:

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['Добавить список доступных машин', 'Список заказов']
        keyboard.add(*buttons)

        await message.answer("Приветствую админ" + message.from_user.full_name, reply_markup=keyboard)


# client_code
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['🗓 Онлайн-договор', '🎁 Акции и новости', '☎️ Колл-центр', 'Доступные 🚘']
        keyboard.add(*buttons)

        await message.answer(
            md.text(
                md.text('Добро пожаловать в официальный бот UzAvtoSavdo.\nЧто умеет данный бот:'),
                md.text('- заключить онлайн договор'),
                md.text('- получать информацию об акциях и о новостях компании'),
                md.text('- напрямую связаться с кол центром компании'),
                md.text('- узнавать о наличии моделей'),
                sep='\n\n'
            ),
            parse_mode=ParseMode.MARKDOWN
        )
        await message.answer('Для того чтобы продолжить выберите одно из 👇👇👇', reply_markup=keyboard)

# available cars


@dp.message_handler(Text(equals='Доступные 🚘'))
async def available_car(message: types.message):

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['🗓 Онлайн-договор', '🎁 Акции и новости', '☎️ Колл-центр']
    keyboard.add(*buttons)

    await message.answer_document(open('available_cars.txt', 'rb'), reply_markup=keyboard)

# agrement


@dp.message_handler(Text(equals='🗓 Онлайн-договор'))
async def dogovor(message: types.Message):

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Фото пасспорта📷', 'Главное меню🧾']
    keyboard.add(*buttons)

    await message.answer(message.from_user.full_name +
                         ', нам необходима фотография Вашего Пасспорта и Ваш телефон номер',
                         reply_markup=keyboard)

# call_center
@dp.message_handler(Text(equals='☎️ Колл-центр'))
async def call_center(message: types.Message):

    await message.answer('+99890 123 45 67')


# sale_news
@dp.message_handler(Text(equals='🎁 Акции и новости'))
async def sale_news(message: types.Message):

    await message.answer('Нет'
                         ' никаких новостей')


# Main menu


@dp.message_handler(Text(equals='Главное меню🧾'))
async def main_menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['🗓 Онлайн-договор', '🎁 Акции и новости', '☎️ Колл-центр', 'Доступные 🚘']
    keyboard.add(*buttons)

    await message.answer('Для того чтобы продолжить выберите одно из 👇👇👇', reply_markup=keyboard)


# passport
@dp.message_handler(Text(equals='Фото пасспорта📷'))
async def passport_img(message: types.Message):

    await message.answer('Пожалуйста, отправтье фотографию вашего пасспорта', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(content_types='photo')
async def telephone(message: types.Message):
    await Form.contact.set()

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Отправить номер телефона", request_contact=True))

    await message.answer('Отлично. Теперь отправтье ваш телефон номер.', reply_markup=keyboard)
    await message.photo[-1].download(destination_dir="photo")


@dp.message_handler(content_types='contact', state=Form.contact)
async def success_reg(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['contact'] = message.contact.phone_number

    await Form.next()

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Spark (от 94 538 000,00 UZS)',
               'Nexia3(от 109 025 000,00 UZS)',
               'Cobalt(от 115 445 000,00 UZS)',
               'Gentra(от 115 607 000,00 UZS)']

    keyboard.add(*buttons)

    await message.answer('✅Спаибо. Ваше данные сохранены.\n Теперь давайте выберем 🚘')
    await message.answer('Выберите одно из моделей', reply_markup=keyboard)

# Spark


@dp.message_handler(Text(equals='Spark (от 94 538 000,00 UZS)'), state=Form.car)
async def spark(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['car'] = message.text

    await Form.next()

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['M-ELEGANT/AT-PLUS 94 538 000,00 UZS']
    keyboard.add(*buttons)

    await message.answer('Выберите комплектацию', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in ['M-ELEGANT/AT-PLUS 94 538 000,00 UZS'], state=Form.level)
async def level_spark(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['level'] = message.text

    await Form.next()

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Summit White⚪️', 'Swichblade Silver🔘', 'Misty Lake🔵', 'Red - E or Not🔴', 'Burnt Coconut🟤']
    keyboard.add(*buttons)

    await message.answer('Выберите цвет 🚘.', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in ['Summit White⚪️', 'Swichblade Silver🔘', 'Misty Lake🔵',
                                                     'Red - E or Not🔴', 'Burnt Coconut🟤'],
                    state=Form.color)
async def color_spark(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['color'] = message.text

    await Form.next()

    if message.text == 'Summit White⚪️':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['🔙Назад', 'Выбрать способ оплаты💰']
        keyboard.add(*buttons)

        await bot.send_photo(message.from_user.id, types.InputFile('cars\spark\spark_white.jpg'),
                             '🕹 Позиция: M-ELEGANT/AT PLUS\n'
                             '💵 Цена: 94 538 000,00 сўм\n'
                             '🛢 Расход на 100 км: 6.2/8.2 л.\n'
                             '💪 Мощность: 85\n'
                             '⚙️ Трансмиссия: AT4\n'
                             '🌈 Цвет: Summit White',
                             reply_markup=keyboard
                             )

        await message.answer('Выберите цвет 🚘. Текущий цвет: Белый.')

    elif message.text == 'Swichblade Silver🔘':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['🔙Назад', 'Выбрать способ оплаты💰']
        keyboard.add(*buttons)

        await bot.send_photo(message.from_user.id, types.InputFile('cars\spark\spark_gray.jpg'),
                             '🕹 Позиция: M-ELEGANT/AT PLUS\n'
                             '💵 Цена: 94 538 000,00 сўм\n'
                             '🛢 Расход на 100 км: 6.2/8.2 л.\n'
                             '💪 Мощность: 85\n'
                             '⚙️ Трансмиссия: AT4\n'
                             '🌈 Цвет: Swichblade Silver',
                             reply_markup=keyboard
                             )

        await message.answer('Выберите цвет 🚘. Текущий цвет: Серый.')

    elif message.text == 'Misty Lake🔵':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['🔙Назад', 'Выбрать способ оплаты💰']
        keyboard.add(*buttons)

        await bot.send_photo(message.from_user.id, types.InputFile('cars\spark\spark_delfin.jpg'),
                             '🕹 Позиция: M-ELEGANT/AT PLUS\n'
                             '💵 Цена: 94 538 000,00 сўм\n'
                             '🛢 Расход на 100 км: 6.2/8.2 л.\n'
                             '💪 Мощность: 85\n'
                             '⚙️ Трансмиссия: AT4\n'
                             '🌈 Цвет: Misty Lake',
                             reply_markup=keyboard
                             )

        await message.answer('Выберите цвет 🚘. Текущий цвет: Синий.')

    elif message.text == 'Red - E or Not🔴':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['🔙Назад', 'Выбрать способ оплаты💰']
        keyboard.add(*buttons)

        await bot.send_photo(message.from_user.id, types.InputFile('cars\spark\spark_red.jpg'),
                             '🕹 Позиция: M-ELEGANT/AT PLUS\n'
                             '💵 Цена: 94 538 000,00 сўм\n'
                             '🛢 Расход на 100 км: 6.2/8.2 л.\n'
                             '💪 Мощность: 85\n'
                             '⚙️ Трансмиссия: AT4\n'
                             '🌈 Цвет: Red - E or Not',
                             reply_markup=keyboard
                             )

        await message.answer('Выберите цвет 🚘. Текущий цвет: Красный.')

    elif message.text == 'Burnt Coconut🟤':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['🔙Назад', 'Выбрать способ оплаты💰']
        keyboard.add(*buttons)

        await bot.send_photo(message.from_user.id, types.InputFile('cars\spark\spark_choco.jpg'),
                             '🕹 Позиция: M-ELEGANT/AT PLUS\n'
                             '💵 Цена: 94 538 000,00 сўм\n'
                             '🛢 Расход на 100 км: 6.2/8.2 л.\n'
                             '💪 Мощность: 85\n'
                             '⚙️ Трансмиссия: AT4\n'
                             '🌈 Цвет: Burnt Coconut',
                             reply_markup=keyboard
                             )

        await message.answer('Выберите цвет 🚘. Текущий цвет: Коричневый.')

# Nexia3


@dp.message_handler(Text(equals='Nexia3(от 109 025 000,00 UZS)'), state=Form.car)
async def nexia3(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['car'] = message.text

    await Form.next()

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['AV-ELEGANT/AT PLUS (109 025 000,00 сўм)']
    keyboard.add(*buttons)

    await message.answer('Выберите комплектацию', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in ['AV-ELEGANT/AT PLUS (109 025 000,00 сўм)'],
                    state=Form.level)
async def level_nexia3(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['level'] = message.text

    await Form.next()

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Summit Whitе⚪️', 'SwichbladE Silvеr🔘', 'Misty LAkе🔵', 'Red - Е or NOt🔴', 'Burnt COcоnut🟤']
    keyboard.add(*buttons)

    await message.answer('Выберите цвет 🚘.', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in ['Summit Whitе⚪️', 'SwichbladE Silvеr🔘', 'Misty LAkе🔵',
                                                     'Red - Е or NOt🔴', 'Burnt COcоnut🟤'],
                    state=Form.color)
async def color_nexia3(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['color'] = message.text

    await Form.next()

    if message.text == 'Summit Whitе⚪️':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['🔙Назад', 'Выбрать способ оплаты💰']
        keyboard.add(*buttons)

        await bot.send_photo(message.from_user.id, types.InputFile('cars\exia3\exia3_white.jpg'),
                             '🕹 Позиция: AV-ELEGANT/AT PLUS\n'
                             '💵 Цена: 109 025 000,00 сўм\n'
                             '🛢 Расход на 100 км: 8/9.3 л.\n'
                             '💪 Мощность: 105\n'
                             '⚙️ Трансмиссия: MT5/AT6\n'
                             '🌈 Цвет: Summit White',
                             reply_markup=keyboard
                             )

        await message.answer('Выберите цвет 🚘. Текущий цвет: Белый.')

    elif message.text == 'SwichbladE Silvеr🔘':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['🔙Назад', 'Выбрать способ оплаты💰']
        keyboard.add(*buttons)

        await bot.send_photo(message.from_user.id, types.InputFile('cars\exia3\exia3_grey.jpg'),
                             '🕹 Позиция: AV-ELEGANT/AT PLUS\n'
                             '💵 Цена: 109 025 000,00 сўм\n'
                             '🛢 Расход на 100 км: 8/9.3 л.\n'
                             '💪 Мощность: 105\n'
                             '⚙️ Трансмиссия: MT5/AT6\n'
                             '🌈 Цвет: Swichblade Silver',
                             reply_markup=keyboard
                             )

        await message.answer('Выберите цвет 🚘. Текущий цвет: Серый.')

    elif message.text == 'Misty LAkе🔵':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['🔙Назад', 'Выбрать способ оплаты💰']
        keyboard.add(*buttons)

        await bot.send_photo(message.from_user.id, types.InputFile('cars\exia3\exia3_delfin.jpg'),
                             '🕹 Позиция: AV-ELEGANT/AT PLUS\n'
                             '💵 Цена: 109 025 000,00 сўм\n'
                             '🛢 Расход на 100 км: 8/9.3 л.\n'
                             '💪 Мощность: 105\n'
                             '⚙️ Трансмиссия: MT5/AT6\n'
                             '🌈 Цвет: Misty Lake',
                             reply_markup=keyboard
                             )

        await message.answer('Выберите цвет 🚘. Текущий цвет: Синий.')

    elif message.text == 'Red - Е or NOt🔴':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['🔙Назад', 'Выбрать способ оплаты💰']
        keyboard.add(*buttons)

        await bot.send_photo(message.from_user.id, types.InputFile('cars\exia3\exia3_red.jpg'),
                             '🕹 Позиция: AV-ELEGANT/AT PLUS\n'
                             '💵 Цена: 109 025 000,00 сўм\n'
                             '🛢 Расход на 100 км: 8/9.3 л.\n'
                             '💪 Мощность: 105\n'
                             '⚙️ Трансмиссия: MT5/AT6\n'
                             '🌈 Цвет: Red - E or Not',
                             reply_markup=keyboard
                             )

        await message.answer('Выберите цвет 🚘. Текущий цвет: Красный.')

    elif message.text == 'Burnt COcоnut🟤':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['🔙Назад', 'Выбрать способ оплаты💰']
        keyboard.add(*buttons)

        await bot.send_photo(message.from_user.id, types.InputFile('cars\exia3\exia3_choco.jpg'),
                             '🕹 Позиция: AV-ELEGANT/AT PLUS\n'
                             '💵 Цена: 109 025 000,00 сўм\n'
                             '🛢 Расход на 100 км: 8/9.3 л.\n'
                             '💪 Мощность: 105\n'
                             '⚙️ Трансмиссия: MT5/AT6\n'
                             '🌈 Цвет: Burnt Coconut',
                             reply_markup=keyboard
                             )

        await message.answer('Выберите цвет 🚘. Текущий цвет: Коричневый.')


# Cobalt


@dp.message_handler(Text(equals='Cobalt(от 115 445 000,00 UZS)'), state=Form.car)
async def cobalt(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['car'] = message.text

    await Form.next()

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['GX/16ATB (4 позиция местной комплектации) (115 445 000,00 сўм)']
    keyboard.add(*buttons)

    await message.answer('Выберите комплектацию', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in ['GX/16ATB (4 позиция местной комплектации) (115 445 000,00 сўм)'],
                    state=Form.level)
async def level_cobalt(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['level'] = message.text

    await Form.next()

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Summit White⚪', 'Swichblade Silvеr🔘', 'Misty Lakе🔵', 'Red - Е or Not🔴', 'Burnt Cocоnut🟤']
    keyboard.add(*buttons)

    await message.answer('Выберите цвет 🚘.', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in ['Summit White⚪', 'Swichblade Silvеr🔘', 'Misty Lakе🔵',
                                                     'Red - Е or Not🔴', 'Burnt Cocоnut🟤'],
                    state=Form.color)
async def color_cobalt(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['color'] = message.text

    await Form.next()

    if message.text == 'Summit White⚪':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['🔙Назад', 'Выбрать способ оплаты💰']
        keyboard.add(*buttons)

        await bot.send_photo(message.from_user.id, types.InputFile('cars\cobalt\cobalt_white.jpg'),
                             '🕹 Позиция: GX/16ATB (4 позиция местной комплектации)\n'
                             '💵 Цена: 115 445 000,00 сўм\n'
                             '🛢 Расход на 100 км:\n' 
                             '💪 Мощность:\n' 
                             '⚙️ Трансмиссия:\n' 
                             '🌈 Цвет: Summit White',
                             reply_markup=keyboard
                             )

        await message.answer('Выберите цвет 🚘. Текущий цвет: Белый.')

    elif message.text == 'Swichblade Silvеr🔘':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['🔙Назад', 'Выбрать способ оплаты💰']
        keyboard.add(*buttons)

        await bot.send_photo(message.from_user.id, types.InputFile('cars\cobalt\cobalt_grey.jpg'),
                             '🕹 Позиция: GX/16ATB (4 позиция местной комплектации)\n'
                             '💵 Цена: 115 445 000,00 сўм\n'
                             '🛢 Расход на 100 км:\n' 
                             '💪 Мощность:\n' 
                             '⚙️ Трансмиссия:\n' 
                             '🌈 Цвет: Swichblade Silver',
                             reply_markup=keyboard
                             )

        await message.answer('Выберите цвет 🚘. Текущий цвет: Серый.')

    elif message.text == 'Misty Lakе🔵':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['🔙Назад', 'Выбрать способ оплаты💰']
        keyboard.add(*buttons)

        await bot.send_photo(message.from_user.id, types.InputFile('cars\cobalt\cobalt_delfin.jpg'),
                             '🕹 Позиция: GX/16ATB (4 позиция местной комплектации)\n'
                             '💵 Цена: 115 445 000,00 сўм\n'
                             '🛢 Расход на 100 км:\n' 
                             '💪 Мощность:\n' 
                             '⚙️ Трансмиссия:\n' 
                             '🌈 Цвет: Misty Lake',
                             reply_markup=keyboard
                             )

        await message.answer('Выберите цвет 🚘. Текущий цвет: Синий.')

    elif message.text == 'Red - Е or Not🔴':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['🔙Назад', 'Выбрать способ оплаты💰']
        keyboard.add(*buttons)

        await bot.send_photo(message.from_user.id, types.InputFile('cars\cobalt\cobalt_red.jpg'),
                             '🕹 Позиция: GX/16ATB (4 позиция местной комплектации)\n'
                             '💵 Цена: 115 445 000,00 сўм\n'
                             '🛢 Расход на 100 км:\n' 
                             '💪 Мощность:\n' 
                             '⚙️ Трансмиссия:\n' 
                             '🌈 Цвет: Red - E or Not',
                             reply_markup=keyboard
                             )

        await message.answer('Выберите цвет 🚘. Текущий цвет: Красный.')

    elif message.text == 'Burnt Cocоnut🟤':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['🔙Назад', 'Выбрать способ оплаты💰']
        keyboard.add(*buttons)

        await bot.send_photo(message.from_user.id, types.InputFile('cars\cobalt\cobalt_choco.jpg'),
                             '🕹 Позиция: GX/16ATB (4 позиция местной комплектации)\n'
                             '💵 Цена: 115 445 000,00 сўм\n'
                             '🛢 Расход на 100 км:\n' 
                             '💪 Мощность:\n' 
                             '⚙️ Трансмиссия:\n' 
                             '🌈 Цвет: Burnt Coconut',
                             reply_markup=keyboard
                             )

        await message.answer('Выберите цвет 🚘. Текущий цвет: Коричневый.')

# Gentra


@dp.message_handler(Text(equals='Gentra(от 115 607 000,00 UZS)'), state=Form.car)
async def gentra(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['car'] = message.text

    await Form.next()

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['L-ELEGANT/AT PLUS (138 126 000,00 сўм)']
    keyboard.add(*buttons)

    await message.answer('Выберите комплектацию', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in ['L-ELEGANT/AT PLUS (138 126 000,00 сўм)'],
                    state=Form.level)
async def level_gentra(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['level'] = message.text

    await Form.next()

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Summit Whitе⚪', 'Swichblаde Silvеr🔘', 'Mistу Lakе🔵', 'Rеd - Е or Not🔴', 'Вurnt Cocоnut🟤']
    keyboard.add(*buttons)

    await message.answer('Выберите цвет 🚘.', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in ['Summit Whitе⚪', 'Swichblаde Silvеr🔘', 'Mistу Lakе🔵',
                                                     'Rеd - Е or Not🔴', 'Вurnt Cocоnut🟤'],
                    state=Form.color)
async def color_gentra(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['color'] = message.text

    await Form.next()

    if message.text == 'Summit Whitе⚪':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['🔙Назад', 'Выбрать способ оплаты💰']
        keyboard.add(*buttons)

        await bot.send_photo(message.from_user.id, types.InputFile('cars\gentra\gentra_white.jpg'),
                             '🕹 Позиция: L-ELEGANT/AT PLUS\n'
                             '💵 Цена: 138 126 000,00 сўм\n'
                             '🛢 Расход на 100 км:7,5\n' 
                             '💪 Мощность:107\n' 
                             '⚙️ Трансмиссия:6АКПП\n' 
                             '🌈 Цвет: Summit White',
                             reply_markup=keyboard
                             )

        await message.answer('Выберите цвет 🚘. Текущий цвет: Белый.')

    elif message.text == 'Swichblаde Silvеr🔘':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['🔙Назад', 'Выбрать способ оплаты💰']
        keyboard.add(*buttons)

        await bot.send_photo(message.from_user.id, types.InputFile('cars\gentra\gentra_grey.jpg'),
                             '🕹 Позиция: L-ELEGANT/AT PLUS\n'
                             '💵 Цена: 138 126 000,00 сўм\n'
                             '🛢 Расход на 100 км:7,5\n' 
                             '💪 Мощность:107\n' 
                             '⚙️ Трансмиссия:6АКПП\n' 
                             '🌈 Цвет: Swichblade Silver',
                             reply_markup=keyboard
                             )

        await message.answer('Выберите цвет 🚘. Текущий цвет: Серый.')

    elif message.text == 'Mistу Lakе🔵':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['🔙Назад', 'Выбрать способ оплаты💰']
        keyboard.add(*buttons)

        await bot.send_photo(message.from_user.id, types.InputFile('cars\gentra\gentra_delfin.jpg'),
                             '🕹 Позиция: L-ELEGANT/AT PLUS\n'
                             '💵 Цена: 138 126 000,00 сўм\n'
                             '🛢 Расход на 100 км:7,5\n' 
                             '💪 Мощность:107\n' 
                             '⚙️ Трансмиссия:6АКПП\n' 
                             '🌈 Цвет: Misty Lake',
                             reply_markup=keyboard
                             )

        await message.answer('Выберите цвет 🚘. Текущий цвет: Синий.')

    elif message.text == 'Rеd - Е or Not🔴':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['🔙Назад', 'Выбрать способ оплаты💰']
        keyboard.add(*buttons)

        await bot.send_photo(message.from_user.id, types.InputFile('cars\gentra\gentra_red.jpg'),
                             '🕹 Позиция: L-ELEGANT/AT PLUS\n'
                             '💵 Цена: 138 126 000,00 сўм\n'
                             '🛢 Расход на 100 км:7,5\n' 
                             '💪 Мощность:107\n' 
                             '⚙️ Трансмиссия:6АКПП\n' 
                             '🌈 Цвет: Red - E or Not',
                             reply_markup=keyboard
                             )

        await message.answer('Выберите цвет 🚘. Текущий цвет: Красный.')

    elif message.text == 'Вurnt Cocоnut🟤':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['🔙Назад', 'Выбрать способ оплаты💰']
        keyboard.add(*buttons)

        await bot.send_photo(message.from_user.id, types.InputFile('cars\gentra\gentra_choco.jpg'),
                             '🕹 Позиция: L-ELEGANT/AT PLUS\n'
                             '💵 Цена: 138 126 000,00 сўм\n'
                             '🛢 Расход на 100 км:7,5\n' 
                             '💪 Мощность:107\n' 
                             '⚙️ Трансмиссия:6АКПП\n' 
                             '🌈 Цвет: Burnt Coconut',
                             reply_markup=keyboard
                             )

        await message.answer('Выберите цвет 🚘. Текущий цвет: Коричневый.')

# back


@dp.message_handler(Text(equals='🔙Назад', ignore_case=True), state='*')
async def back(message: types.Message, state: FSMContext):

    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)

    await state.finish()

    await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())

    await Form.car.set()

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Spark (от 94 538 000,00 UZS)',
               'Nexia3(от 109 025 000,00 UZS)',
               'Cobalt(от 115 445 000,00 UZS)',
               'Gentra(от 115 607 000,00 UZS)']

    keyboard.add(*buttons)

    await message.answer('Выберите одно из моделей', reply_markup=keyboard)


# pay_via


@dp.message_handler(Text(equals='Выбрать способ оплаты💰'), state=Form.just)
async def back(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['just'] = message.text

    await Form.next()

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Банк🏦', 'Карта💳', 'Наличные💵']
    keyboard.add(*buttons)

    await message.answer('Выберите способ оплаты👇', reply_markup=keyboard)


# creating_txt_of_order


@dp.message_handler(lambda message: message.text in ['Банк🏦', 'Карта💳', 'Наличные💵'], state=Form.pay_via)
async def pay_via_bank(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['pay_via'] = message.text

    await Form.next()

    lines = [
        data['contact'], data['car'], data['color'], data['level'], data['pay_via']
    ]
    linestring = '\n'.join(lines)

    filen = open('list_of_orders.txt', 'w', encoding="utf-8")
    filen.write(linestring)

    if message.text == 'Банк🏦':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['✖️Отменить все действия', 'Подтвердить']
        keyboard.add(*buttons)

        await message.answer('8600 AAAA BBBB CCCC ',
                             reply_markup=keyboard)

    elif message.text == 'Карта💳':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['✖️Отменить все действия', 'Подтвердить']
        keyboard.add(*buttons)

        await message.answer('Успешно',
                             reply_markup=keyboard)

    elif message.text == 'Наличные💵':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['✖️Отменить все действия', 'Подтвердить']
        keyboard.add(*buttons)

        await message.answer('В таком случае посетите один из наших филлиалов',
                             reply_markup=keyboard)

    await bot.send_message(
        1187125731,
        md.text(
            md.text('📞   ', md.bold(data['contact'])),
            md.text('🚘 Модел  ', md.bold(data['car'])),
            md.text('🕹 Позиция  ', md.bold(data['level'])),
            md.text('🌈 Цвет  ', md.bold(data['color'])),
            md.text('💰 Способ оплаты  ', md.bold(data['pay_via'])),
            sep='\n'
        ),
        parse_mode=ParseMode.MARKDOWN,
    )

    await state.finish()


@dp.message_handler(Text(equals='Подтвердить'))
async def apply(message: types.Message):

    await message.answer('Ваша заявка принята')


# cancel_all_detail

@dp.message_handler(Text(equals='✖️Отменить все действия', ignore_case=True), state='*')
async def cancel_all_detail(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)

    await state.finish()

    await message.answer('Все действия отменены.')

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['🗓 Онлайн-договор', '🎁 Акции и новости', '☎️ Колл-центр' 'Список доступных машин']
    keyboard.add(*buttons)

    await message.answer(
        md.text(
            md.text('Добро пожаловать в официальный бот UzAvtoSavdo.\nЧто умеет данный бот:'),
            md.text('- заключить онлайн договор'),
            md.text('- получать информацию об акциях и о новостях компании'),
            md.text('- напрямую связаться с кол центром компании'),
            sep='\n\n'
        ),
        parse_mode=ParseMode.MARKDOWN
    )
    await message.answer('Для того чтобы продолжить выберите одно из 👇👇👇', reply_markup=keyboard)


# Admin_code


# add_available_cars_by_admin
@dp.message_handler(Text(equals='Добавить список доступных машин'))
async def file_write(message: types.Message):
    if message.from_user.id == 1187125731:

        await message.answer("enter available car list")

    else:
        await message.reply("you are not admin")


# List_of_orders
@dp.message_handler(Text(equals='Список заказов'))
async def get_list_of_orders(message: types.Message):

    await bot.send_document(message.chat.id, document=open('list_of_orders.txt', 'rb'))


@dp.message_handler(lambda message: message.text)
async def file(message: types.Message):

    if message.from_user.id == 1187125731:
        cars = str(message.text)

        file = open('available_cars.txt', 'w')
        file.write(cars)
        file.close()

        await message.answer('Успешно сохранен')
        await bot.send_document(message.chat.id, document=open('available_cars.txt', 'rb'))

    else:
        await message.reply('Вы не являетесь Админом!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
