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