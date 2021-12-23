@dp.message_handler(Text(equals='Spark (от 94 538 000,00 UZS)'), state=Form.car)
async def spark(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['car'] = message.text

    await Form.next()

    await message.answer('Выберите комплектацию', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in ['M-ELEGANT/AT-PLUS 94 538 000,00 UZS'], state=Form.level)
async def level_spark(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['level'] = message.text

    await Form.next()

    await message.answer('Выберите цвет 🚘.', reply_markup=keyboard)