@dp.message_handler(Text(equals='Nexia3(от 109 025 000,00 UZS)'), state=Form.car)
async def nexia3(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['car'] = message.text

    await Form.next()

    await message.answer('Выберите комплектацию', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in ['AV-ELEGANT/AT PLUS (109 025 000,00 сўм)'],
                    state=Form.level)
async def level_nexia3(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['level'] = message.text

    await Form.next()

    await message.answer('Выберите цвет 🚘.', reply_markup=keyboard)