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