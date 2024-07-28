from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext



class Buy_order(StatesGroup):
    link = State()
    amount = State()
    confirmation = State()


class CryproBot(StatesGroup):
    sum = State()

class Coupon_activate(StatesGroup):
    coupon = State()