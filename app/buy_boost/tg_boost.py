import requests

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

from keyboards import client as k
from data import users as u
from data import requests as r
from data import services as s

from config import bot, API_KEY
from app.ban_check import handle_blocked_user
from app.fsm import Buy_order


router = Router()



@router.callback_query(k.Menu_callback.filter(F.menu == 'tg_boost'))
async def menu(call: CallbackQuery, callback_data: k.Menu_callback, state: FSMContext):

    try:
        await state.clear()
    except:
        pass

    if await handle_blocked_user(call=call):
        return
    
    photo = FSInputFile('photos/boost.jpg')
    kb = k.tg_prem_views_kb()
    await call.message.answer_photo(photo=photo, reply_markup=kb)



@router.callback_query(k.Buy_info.filter(F.menu == 'tg_boost'))
async def product(call: CallbackQuery, callback_data: k.Buy_info, state: FSMContext):

    if await handle_blocked_user(call=call):
        return

    data_service = await s.get_service_info(service_id=callback_data.service)
    text = f'{data_service[2]}\n\nЦена указана за 1 шт: {data_service[3]}₽'

    kb = k.order_kb(menu=callback_data.menu, service=callback_data.service)
    await call.message.answer(text=text, reply_markup=kb)