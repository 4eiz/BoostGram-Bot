from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

from keyboards import client as k
from data import users as u

from config import bot
from app.ban_check import handle_blocked_user


router = Router()



@router.callback_query(k.Menu_callback.filter(F.menu == 'buy_boost'))
async def menu(call: CallbackQuery, callback_data: k.Menu_callback, state: FSMContext):

    try:
        await state.clear()
    except:
        pass

    
    if await handle_blocked_user(call=call):
        return

    photo = FSInputFile('photos/category.jpg')
    kb = k.category_kb()
    text = '<b>Выберите категорию:</b>'
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=kb)
    