"""
from aiogram import types
import logging
import aiogram.utils.markdown as md
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode
from create_bot import dp, bot
from states.personalData import Form
from keyboards.client_kb import back

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

    await message.answer('Выберите одно из моделей', reply_markup=back)


# pay_via_continue


@dp.message_handler(lambda message: message.text, state=Form.info)
async def info(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['info'] = message.text

    await Form.next()

    await message.answer('Спасбо, Ваша заявка принята. '
                         'С вами свяжутся наши диллеры после обработки информации.')
    await bot.send_message(
        1187125731,
        md.text(
            md.text('📞   ', md.bold(data['contact'])),
            md.text('🚘 Модел  ', md.bold(data['car'])),
            md.text('🕹 Позиция  ', md.bold(data['level'])),
            md.text('🌈 Цвет  ', md.bold(data['color'])),
            md.text('💰 Способ оплаты  ', md.bold(data['pay_via'])),
            md.text('ℹ Инормация  ', md.bold(data['info'])),
            sep='\n'
        ),
        parse_mode=ParseMode.MARKDOWN,
    )

    await state.finish()
"""

import csv

