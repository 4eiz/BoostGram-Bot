from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

from keyboards import client as k
from data import coupons as c

from config import ADMIN


router = Router()




@router.message(Command('coupons'))
async def main(message: Message, command: CommandObject, state: FSMContext):
    try:
        await state.clear()
    except:
        pass
    
    user_id = message.from_user.id
    if user_id != ADMIN:
        return
    
    text = await c.get_all_coupons()
    if text == '':
        text = 'Купонов нет'
    await message.answer(text=text)



@router.message(Command('add_coupon'))
async def change_price(message: Message, command: CommandObject, state: FSMContext):

    arguments = command.args.split(' _ ')
    coupon = arguments[0]
    money = arguments[1]

    await c.add_coupon(coupon=coupon, money=money)


@router.message(Command('del_coupon'))
async def change_price(message: Message, command: CommandObject, state: FSMContext):

    arguments = command.args
    coupon = arguments[0]

    await c.delete_coupon(coupon=coupon)