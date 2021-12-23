from aiogram.dispatcher.filters.state import StatesGroup, State

class Form(StatesGroup):
    contact = State()
    car = State()
    level = State()
    color = State()
    just = State()
    pay_via = State()
    info = State()
