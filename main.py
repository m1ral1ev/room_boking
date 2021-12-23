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
    level = State()
    room = State()
    time = State()
    contact = State()
    user_id = State()
    just = State()
    just1 = State()
    tg_id = State()


# main menu


@dp.message_handler(commands="start")
async def start_cmd(message: types.Message):

    if message.from_user.id == 1187125731:

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['Add a available room list', 'List of orders', 'Answer', 'Reject']
        keyboard.add(*buttons)

        await message.answer("Welcome Admin " + message.from_user.full_name, reply_markup=keyboard)


# Client_code

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['Book the room🏛', 'Get the list of available rooms💡']
        keyboard.add(*buttons)

        await message.answer(
            md.text(
                md.text('Welcome, user.\n:What can I do for you?'),
                md.text('- help to get a room'),
                md.text('- provide you a list of available rooms'),
                sep='\n\n'
            ),
            parse_mode=ParseMode.MARKDOWN
        )
        await message.answer('Choose one option 👇👇👇', reply_markup=keyboard)

# start the booking room
# get the list of available rooms


@dp.message_handler(Text(equals='Get the list of available rooms💡'))
async def available_room_list(message: types.Message):

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Main menu']
    keyboard.add(*buttons)

    await message.answer('Here the list.')
    await bot.send_document(message.chat.id, document=open('available_rooms.txt', 'rb'), reply_markup=keyboard)


# choose level


@dp.message_handler(Text(equals='Book the room🏛'))
async def book_room(message: types.message):

    await Form.level.set()

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['1', '2', '3', '4', '🔙Main menu']
    keyboard.add(*buttons)

    await message.answer('Okay, please choice the level of room👇👇👇:', reply_markup=keyboard)


# choose a room level
# choose a time


@dp.message_handler(lambda message: message.text in ['1', '2', '3', '4'], state=Form.level)
async def level(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['level'] = message.text

    await Form.next()

    if message.text == '1':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['105', '102', '103', '101', '🔙Main menu']
        keyboard.add(*buttons)

        await message.answer('You choose 1 level, now choose the room', reply_markup=keyboard)

        @dp.message_handler(lambda message: message.text in ['105', '102', '103', '101', '🔙Main menu'],
                            state=Form.room)
        async def choose_time(message: types.Message, state: FSMContext):

            async with state.proxy() as data:
                data['room'] = message.text

            await Form.next()

            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            buttons = ['10:00', '11:30', '13:50', '15:20', '16:50']
            keyboard.add(*buttons)

            await message.answer('Now choose a time for book', reply_markup=keyboard)

    elif message.text == '2':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['204', '205', '207', '208', '🔙Main menu']
        keyboard.add(*buttons)

        await message.answer('You choose 2 level, now choose the room', reply_markup=keyboard)

        @dp.message_handler(lambda message: message.text in ['204', '205', '207', '208', '🔙Main menu'],
                            state=Form.room)
        async def choose_time(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['room'] = message.text

            await Form.next()

            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            buttons = ['10:00', '11:30', '13:50', '15:20', '16:50']
            keyboard.add(*buttons)

            await message.answer('Now choose a time for book', reply_markup=keyboard)

    elif message.text == '3':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['302', '305', '303AB', '302AB', '🔙Main menu']
        keyboard.add(*buttons)

        await message.answer('You choose 3 level, now choose the room', reply_markup=keyboard)

        @dp.message_handler(lambda message: message.text in ['302', '305', '303AB', '302AB', '🔙Main menu'],
                            state=Form.room)
        async def choose_time(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['room'] = message.text

            await Form.next()

            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            buttons = ['10:00', '11:30', '13:50', '15:20', '16:50']
            keyboard.add(*buttons)

            await message.answer('Now choose a time for book', reply_markup=keyboard)

    elif message.text == '4':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['405', '406', '403AB', '404AB', '🔙Main menu']
        keyboard.add(*buttons)

        await message.answer('You choose 4 level, now choose the room', reply_markup=keyboard)

        @dp.message_handler(lambda message: message.text in ['405', '406', '403AB', '404AB', '🔙Main menu'],
                            state=Form.room)
        async def choose_time(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['room'] = message.text

            await Form.next()

            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            buttons = ['10:00', '11:30', '13:50', '15:20', '16:50']
            keyboard.add(*buttons)

            await message.answer('Now choose a time for book', reply_markup=keyboard)

    else:

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['1', '2', '3', '4', 'Main menu']
        keyboard.add(*buttons)

        await message.answer('You enter something wrong, please choose the correct level👇👇👇', reply_markup=keyboard)


# choose a room number

@dp.message_handler(lambda message: message.text in ['10:00', '11:30', '13:50', '15:20', '16:50'], state=Form.time)
async def number_of_students(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['time'] = message.text

    await Form.next()

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Share a contact", request_contact=True))

    await message.answer('I need a your contact', reply_markup=keyboard)


# ID of students


@dp.message_handler(content_types='contact', state=Form.contact)
async def check_process(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['contact'] = message.contact.phone_number
        data['tg_id'] = message.from_user.id

    await Form.next()

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['🔙Main menu']
    keyboard.add(*buttons)

    await message.answer('To book the room you should enter ID of 9 students.\n'
                         'But, now enter Your ID', reply_markup=keyboard)
    await message.answer('Example:\n (s)u12345')


# back to main menu


@dp.message_handler(Text(equals='🔙Main menu', ignore_case=True), state='*')
async def back(message: types.Message, state: FSMContext):

    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)

    await state.finish()

    await message.reply('You back to Main menu, all details are cancelled.', reply_markup=types.ReplyKeyboardRemove())

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Book the room🏛', 'Get the list of available rooms💡']
    keyboard.add(*buttons)

    await message.answer(
        md.text(
            md.text('Welcome, user.\n:What can I do for you?'),
            md.text('- help to get a room'),
            md.text('- provide you a list of available rooms'),
            sep='\n\n'
        ),
        parse_mode=ParseMode.MARKDOWN
    )
    await message.answer('Choose one option 👇👇👇', reply_markup=keyboard)


# Admin_code


@dp.message_handler(lambda message: message.text in ['Add a available room list', 'List of orders', 'Answer', 'Reject'],
                    state=Form.just1)
async def file_write(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['just1'] = message.text

    await Form.next()

    if message.text == 'Add a available room list':
        if message.from_user.id == 1187125731:
            await message.answer("Enter available room(s): ", reply_markup=types.ReplyKeyboardRemove())
        else:
            await message.reply("You are not admin!")

    elif message.text == 'List of orders':
        if message.from_user.id == 1187125731:
            await bot.send_document(message.chat.id, document=open('list_of_orders.txt', 'rb'))
        else:
            await message.reply("You are not admin!")

    elif message.text == 'Answer':
        if message.from_user.id == 1187125731:
            chat = data['tg_user']
            await bot.send_message(chat, 'Dear student you can take your room')
        else:
            await message.reply("You are not admin!")

    elif message.text == 'Reject':
        if message.from_user.id == 1187125731:
            chat = data['tg_user']
            await bot.send_message(chat, 'Dear student, you CANNOT take your room')
        else:
            await message.reply("You are not admin!")

@dp.message_handler(lambda message: message.text)
async def file(message: types.Message):

    if message.from_user.id == 1187125731:
        rooms = str(message.text)

        file = open('available_room.txt', 'w')
        file.write(rooms)
        file.close()

        await message.answer('Saved!')
        await bot.send_document(message.chat.id, document=open('available_room.txt', 'rb'))


# check a user_ID from DB


@dp.message_handler(lambda message: message.text, state=Form.user_id)
async def check_process(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['user_id'] = message.text

    await Form.next()

    new_file = open("students.txt")
    id_info = list()
    for line in new_file:
        words = line.split()
        id_info.extend(words)
    await bot.send_message(message.chat.id, 'I check your ID in my DB')
    print(id_info)

    name = message.text
    if name in id_info:

        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = ['Enter a ID of 9 students', '❌Cancel all']
        keyboard1.add(*button1)

        await message.answer('Okay, i have your ID in my DB', reply_markup=keyboard1)
        print('true')

    else:

        keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button2 = ['🔙Main menu']
        keyboard2.add(*button2)

        id_inf = ''.join(id_info)
        await message.answer("ID has not found in my DB! Contact to 408 room", reply_markup=keyboard2)
        print('No such ID in: ' + id_inf)


@dp.message_handler(Text(equals='❌Cancel all', ignore_case=True), state='*')
async def cancell_all(message: types.Message, state: FSMContext):

    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)

    await state.finish()

    await message.reply('You cancell all, details are cancelled.', reply_markup=types.ReplyKeyboardRemove())

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Book the room🏛', 'Get the list of available rooms💡']
    keyboard.add(*buttons)

    await message.answer(
        md.text(
            md.text('Welcome, user.\n:What can I do for you?'),
            md.text('- help to get a room'),
            md.text('- provide you a list of available rooms'),
            sep='\n\n'
        ),
        parse_mode=ParseMode.MARKDOWN
    )
    await message.answer('Choose one option 👇👇👇', reply_markup=keyboard)

@dp.message_handler(Text(equals='Enter a ID of 9 students'), state=Form.just)
async def id_9students(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['just'] = message.text

    await Form.next()

    new_file = open("students.txt")
    id_info = list()
    for line in new_file:
        words = line.split()
        id_info.extend(words)

    count = 0
    for i in range(3):
        name = input('Enter ID')
        if name in id_info:
            count += 1
            print(count)

        else:
            print("ID has not found!")

    await bot.send_message(
        1187125731,
        md.text(
            md.text('📞   : ', md.bold(data['contact'])),
            md.text('Level: ', md.bold(data['level'])),
            md.text('Room: ', md.bold(data['room'])),
            md.text('Time: ', md.bold('time')),
            md.text('ID of student: ', md.bold(data['user_id'])),
            md.text('Telegram ID: ', md.bold(data['tg_id'])),
            sep='\n'
        ),
        parse_mode=ParseMode.MARKDOWN,
    )

    lines = [
        data['contact'], data['user_id'], data['level'], data['room'], data['time']
    ]
    linestring = '\n'.join(lines)

    filen = open('list_of_orders.txt', 'a', encoding="utf-8")
    filen.write('From '+'{}\n'.format(data['tg_id']))
    filen.write(linestring)

    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
"""
# creating_txt_of_order

    lines = [
        data['contact'], data['level'], data['room'], data['time']
    ]
    linestring = '\n'.join(lines)

    filen = open('list_of_orders.txt', 'w', encoding="utf-8")
    filen.write(linestring)
"""
