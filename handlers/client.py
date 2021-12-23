from aiogram import types
import aiogram.utils.markdown as md
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode
from create_bot import dp
from states.personalData import Form
from keyboards.client_kb import main_menu, available_cars, agreement, Main_menu, Request_contact, car_type, pay_via

# main menu


@dp.message_handler(commands="start")
async def start_cmd(message: types.Message):

    await message.answer(
        md.text(
            md.text('Добро пожаловать в официальный бот UzAutoSavdo.\nЧто умеет данный бот:'),
            md.text('- заключить онлайн договор'),
            md.text('- получать информацию об акциях и о новостях компании'),
            md.text('- напрямую связаться с кол центром компании'),
            md.text('- узнавать о наличии моделей'),
            sep='\n\n'
        ),
        parse_mode=ParseMode.MARKDOWN
    )
    await message.answer('Для того чтобы продолжить выберите одно из 👇👇👇', reply_markup=main_menu)


# available cars


@dp.message_handler(Text(equals='Доступные 🚘'))
async def available_car(message: types.message):

    await message.answer_document(open('available_cars.docx', 'rb'), reply_markup=available_cars)


# agreement


@dp.message_handler(Text(equals='🗓 Онлайн-договор'))
async def dogovor(message: types.Message):

    await message.answer(message.from_user.full_name +
                         ', нам необходима фотография Вашего Пасспорта и Ваш телефон номер',
                         reply_markup=agreement)


# Main menu


@dp.message_handler(Text(equals='Главное меню🧾'))
async def main_menu(message: types.Message):

    await message.answer('Для того чтобы продолжить выберите одно из 👇👇👇', reply_markup=Main_menu)


# Passport photo

@dp.message_handler(Text(equals='Фото пасспорта📷'))
async def passport_img(message: types.Message):

    await message.answer('Пожалуйста, отправтье фотографию вашего пасспорта', reply_markup=types.ReplyKeyboardRemove())


# Request_contact


@dp.message_handler(content_types='photo')
async def telephone(message: types.Message):
    await Form.contact.set()

    await message.answer('Отлично. Теперь отправтье ваш телефон номер.', reply_markup=Request_contact)
    await message.photo[-1].download(destination_dir="photo")


# car_type


@dp.message_handler(content_types='contact', state=Form.contact)
async def success_reg(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['contact'] = message.contact.phone_number

    await Form.next()

    await message.answer('✅Спаибо. Ваше данные сохранены.\n Теперь давайте выберем 🚘')
    await message.answer('Выберите одно из моделей', reply_markup=car_type)


# pay_via


@dp.message_handler(Text(equals='Выбрать способ оплаты💰'), state=Form.just)
async def pay(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['just'] = message.text

    await Form.next()

    await message.answer('Выберите способ оплаты👇', reply_markup=pay_via)


# pay_via_continue


@dp.message_handler(lambda message: message.text in ['Банк🏦', 'Карта💳', 'Наличные💵'], state=Form.pay_via)
async def pay_via(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['pay_via'] = message.text

    await Form.next()

    if message.text == 'Банк🏦':

        await message.answer('Пожалуйста, корректно введите Ваши банковские данные: ',
                             reply_markup=types.ReplyKeyboardRemove())

    elif message.text == 'Карта💳':

        await message.answer('Наш универсальный номер карты:\n8600 AAAA BBBB CCCC')
        await message.answer('Для того чтобы в дальнейшем не было недрозумений, '
                             'пожалуйста при переводе денег посетите наш диллерский салон',
                             reply_markup=types.ReplyKeyboardRemove())

    elif message.text == 'Наличные💵':

        await message.answer('В таком случае посетите один из наших филлиалов',
                             reply_markup=types.ReplyKeyboardRemove())
