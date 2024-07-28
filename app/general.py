from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

from keyboards import client as k
from data import users as u

from app.ban_check import handle_blocked_user



router = Router()



@router.message(CommandStart())
async def start(message: Message, state: FSMContext):

    try:
        await state.clear()
    except:
        pass
    
    user_id = message.from_user.id
    user = await u.get_user_info(user_id=user_id)

    if user == None:
        await u.add_user(user_id=user_id)
        ban_status = 0
    else:
        ban_status = user[3]
    
    if ban_status == 1:
        text = '<b>Вы заблокированны в боте</b>'
        kb = k.support_kb()
        await message.answer(text=text, reply_markup=kb)
        return
    
    photo = FSInputFile('photos/menu.jpg')
    kb = k.menu_kb()
    await message.answer_photo(photo=photo, reply_markup=kb)





@router.callback_query(k.Menu_callback.filter(F.menu == 'menu'))
async def menu(call: CallbackQuery, callback_data: k.Menu_callback, state: FSMContext):

    try:
        await state.clear()
    except:
        pass



    if await handle_blocked_user(call=call):
        return
    
    photo = FSInputFile('photos/menu.jpg')
    kb = k.menu_kb()
    await call.message.answer_photo(photo=photo, reply_markup=kb)