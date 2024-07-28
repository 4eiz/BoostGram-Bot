from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

from keyboards import client as k
from data import services as s

from config import bot, ADMIN
from app.ban_check import handle_blocked_user


router = Router()




@router.message(Command('services'))
async def main(message: Message, command: CommandObject, state: FSMContext):
    try:
        await state.clear()
    except:
        pass
    
    user_id = message.from_user.id
    if user_id != ADMIN:
        return
    
    text = await s.get_all_services()
    await message.answer(text=text)




@router.message(Command('price'))
async def change_price(message: Message, command: CommandObject, state: FSMContext):

    arguments = command.args.split(' _ ')
    service_id = arguments[0]
    price = arguments[1]

    await s.update_price(service_id=service_id, price=price)


@router.message(Command('name'))
async def change_price(message: Message, command: CommandObject, state: FSMContext):

    arguments = command.args.split(' _ ')
    service_id = arguments[0]
    text = arguments[1]

    # print(f'СЕРВИС: {service_id}')
    # print(f'ТЕКСТ: {text}')

    await s.update_name(service_id=service_id, new_name=text)