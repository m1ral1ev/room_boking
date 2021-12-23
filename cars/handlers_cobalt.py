from create_bot import dp


@dp.message_handler(Text(equals='Cobalt(от 115 445 000,00 UZS)'), state=Form.car)
async def cobalt(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['car'] = message.text

    await Form.next()

    await message.answer('Выберите комплектацию', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in ['GX/16ATB (4 позиция местной комплектации) (115 445 000,00 сўм)'],
                    state=Form.level)
async def level_cobalt(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['level'] = message.text

    await Form.next()

    await message.answer('Выберите цвет 🚘.', reply_markup=keyboard)