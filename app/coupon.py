from aiogram import Router
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from keyboards import client as k
from data import users as u

from config import bot
from app.ban_check import handle_blocked_user
from app.fsm import Coupon_activate


router = Router()




@router.callback_query(k.Menu_callback.filter(F.menu == 'coupon'))
async def menu(call: CallbackQuery, callback_data: k.Menu_callback, state: FSMContext):

    if await handle_blocked_user(call=call):
        return
    
    kb = k.cancel_kb()

    text = 'Введите купон'
    await call.message.answer(text=text, reply_markup=kb)
    await state.set_state(Coupon_activate.coupon)



@router.message(Coupon_activate.coupon)
async def show(message: Message, state: FSMContext):

    user_id = message.from_user.id
    coupon = message.text
    status = await u.activate_coupon(user_id=user_id, coupon_id=coupon)
    if status == 1:
        text = 'Купон уже был использован.'
    elif status == 2:
        text = 'Купон не найден.'
    elif status == 3:
        text = 'Купон успешно активирован!'

    await message.answer(text=text)