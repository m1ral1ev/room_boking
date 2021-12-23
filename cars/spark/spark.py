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

        await bot.send_photo(message.from_user.id, types.InputFile('spark\spark_white.jpg'),
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

        await bot.send_photo(message.from_user.id, types.InputFile('spark\spark_gray.jpg'),
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

        await bot.send_photo(message.from_user.id, types.InputFile('spark\spark_delfin.jpg'),
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

        await bot.send_photo(message.from_user.id, types.InputFile('spark\spark_red.jpg'),
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

        await bot.send_photo(message.from_user.id, types.InputFile('spark\spark_choco.jpg'),
                             '🕹 Позиция: M-ELEGANT/AT PLUS\n'
                             '💵 Цена: 94 538 000,00 сўм\n'
                             '🛢 Расход на 100 км: 6.2/8.2 л.\n'
                             '💪 Мощность: 85\n'
                             '⚙️ Трансмиссия: AT4\n'
                             '🌈 Цвет: Burnt Coconut',
                             reply_markup=keyboard
                             )

        await message.answer('Выберите цвет 🚘. Текущий цвет: Коричневый.')