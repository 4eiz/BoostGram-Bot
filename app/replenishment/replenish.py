from aiocryptopay import AioCryptoPay
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.ban_check import handle_blocked_user
from keyboards import client as k
from app.fsm import CryproBot



router = Router()



@router.callback_query(k.Menu_callback.filter(F.menu == 'replenish'))
async def rep1(call: CallbackQuery, callback_data: k.Menu_callback, state: FSMContext):

    text = '<b>Выберите способ пополнения</b>'

    kb = k.replenishment_kb()

    if await handle_blocked_user(call=call):
        return
    await call.message.answer(text=text, reply_markup=kb)




@router.callback_query(k.Menu_callback.filter(F.menu == 'cryptobot'))
async def rep1(call: CallbackQuery, callback_data: k.Menu_callback, state: FSMContext):

    text = '<b>🔢 Введите сумму для пополнения баланса</b>'
    id = call.message.message_id

    await state.update_data(del_mes_id=id)
    await call.message.edit_text(text, reply_markup=k.cancel_kb())
    await state.set_state(CryproBot.sum)