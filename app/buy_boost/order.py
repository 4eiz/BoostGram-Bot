import requests

from aiogram import Router
from aiogram.types import Message
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards import client as k
from data import users as u
from data import requests as r
from data import services as s

from config import bot, API_KEY
from app.ban_check import handle_blocked_user
from app.fsm import Buy_order


router = Router()



@router.callback_query(k.Buy_info.filter(F.menu == 'order'))
async def make_order(call: CallbackQuery, callback_data: k.Buy_info, state: FSMContext):

    if await handle_blocked_user(call=call):
        return

    await state.update_data(service=callback_data.service)

    text = '<b>Укажите ссылку на ваш канал/чат</b>'
    kb = k.cancel_kb()
    await call.message.answer(text=text, reply_markup=kb)
    await state.set_state(Buy_order.link)



@router.message(Buy_order.link)
async def get_link(message: Message, state: FSMContext):

    if type(message.text) != str:
        return

    await state.update_data(link=message.text)

    text = '<b>Укажите количество</b>'
    kb = k.cancel_kb()
    await message.answer(text=text, reply_markup=kb)
    await state.set_state(Buy_order.amount)



@router.message(Buy_order.amount)
async def get_amount(message: Message, state: FSMContext):
    try:
        amount = int(message.text)
        await state.update_data(amount=amount)
    except:
        text = f'<b>Укажите количество</b>'
        kb = k.cancel_kb()
        await message.answer(text=text, reply_markup=kb)
        return
    

    data = await state.get_data()

    link = data.get('link')
    service = data.get('service')

    data_service = await s.get_service_info(service_id=service)
    price = amount * data_service[3]
    price = round(price, 3)

    text = f'<b>Подтвердите ваш заказ\n\nСсылка: {link}\nКоличество: {amount}\n\nЦена: {price}₽</b>'
    kb = k.conf_kb()
    await message.answer(text=text, reply_markup=kb)
    await state.set_state(Buy_order.confirmation)


@router.callback_query(k.Menu_callback.filter(F.menu == 'confirmation'), Buy_order.confirmation)
async def get_confirmation(call: CallbackQuery, callback_data: k.Menu_callback, state: FSMContext):

    chat_id = call.from_user.id
    message_id = call.message.message_id
    await bot.delete_message(chat_id, message_id)

    user_id = call.from_user.id
    data = await state.get_data()

    service = data.get('service')
    amount = data.get('amount')
    link = data.get('link')

    data_service = await s.get_service_info(service_id=service)
    price = amount * data_service[3]
    price = round(price, 3)

    payment = await u.update_balance(user_id=user_id, amount=-price)
    if payment == False:
        text = '<b>Недостаточно средств</b>'
        await call.message.answer(text=text)
        await state.clear()
        return

    url_api = f'https://teateagram.com/api/v2?action=add&service={service}&link={link}&quantity={amount}&key={API_KEY}'
    response = requests.get(url=url_api)


    # Преобразование JSON-ответа в словарь
    response_data = response.json()
    print(response_data)
    if 'error' in response_data:
        text = '<b>Укажите большее или меньшее количество</b>'
        await call.message.answer(text=text)
        payment = await u.update_balance(user_id=user_id, amount=price)

    elif 'order' in response_data:
        order_id = response_data['order']
        text = f'<b>Заказ {order_id} успешно создан</b>'
        await call.message.answer(text=text)
        await r.add_request(order_id=order_id,price=price, user_id=user_id, status=True)
        await u.update_total_orders(user_id=user_id, amount=1)

    await state.clear()