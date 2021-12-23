    from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# main menu

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🗓 Онлайн-договор')
        ],
        [
            KeyboardButton(text='🎁 Акции и новости')
        ],
        [
            KeyboardButton(text='☎️ Колл-центр')
        ],
        [
            KeyboardButton(text='Доступные 🚘')
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)

# available cars

available_cars = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🗓 Онлайн-договор')
        ],
        [
            KeyboardButton(text='🎁 Акции и новости')
        ],
        [
            KeyboardButton(text='☎️ Колл-центр')
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)

# agreement

agreement = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Фото пасспорта📷')
        ],
        [
            KeyboardButton(text='Главное меню🧾')
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)

# Main menu

Main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🗓 Онлайн-договор')
        ],
        [
            KeyboardButton(text='🎁 Акции и новости')
        ],
        [
            KeyboardButton(text='☎️ Колл-центр')
        ],
        [
            KeyboardButton(text='Доступные 🚘')
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)

# Request_contact

Request_contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Отправить номер телефона', request_contact=True)
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)

# car_type

car_type = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Spark (от 94 538 000,00 UZS)')
        ],
        [
            KeyboardButton(text='Nexia3(от 109 025 000,00 UZS)')
        ],
        [
            KeyboardButton(text='Cobalt(от 115 445 000,00 UZS)')
        ],
        [
            KeyboardButton(text='Gentra(от 115 607 000,00 UZS)')
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)

# back

back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Spark (от 94 538 000,00 UZS)')
        ],
        [
            KeyboardButton(text='Nexia3(от 109 025 000,00 UZS)')
        ],
        [
            KeyboardButton(text='Cobalt(от 115 445 000,00 UZS)')
        ],
        [
            KeyboardButton(text='Gentra(от 115 607 000,00 UZS)')
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)

# pay_via

pay_via = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Банк🏦')
        ],
        [
            KeyboardButton(text='Карта💳')
        ],
        [
            KeyboardButton(text='Наличные💵')
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)
