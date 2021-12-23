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