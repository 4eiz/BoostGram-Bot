from aiogram import Router
from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

from keyboards import client as k
from data import users as u

from config import bot
from app.ban_check import handle_blocked_user



router = Router()




@router.callback_query(k.Menu_callback.filter(F.menu == 'profile'))
async def menu(call: CallbackQuery, callback_data: k.Menu_callback, state: FSMContext):

    if await handle_blocked_user(call=call):
        return
    
    user_id = call.from_user.id
    user_data = await u.get_user_info(user_id=user_id)
    photo = FSInputFile('photos/profile.jpg')
    kb = k.profile_kb()

    text = f'''<b>Ваш ID: <code>{user_data[0]}</code> 
Ваш баланс: <code>{round(user_data[1], 3)}₽</code>
Ваши заказы: <code>{user_data[2]}</code></b>'''
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=kb)