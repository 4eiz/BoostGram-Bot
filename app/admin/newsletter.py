from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

from keyboards import client as k
from data import admin as a

from config import bot, ADMIN



router = Router()




@router.message(Command('newsletter'))
async def change_price(message: Message, command: CommandObject, state: FSMContext):

    user_id = message.from_user.id
    if user_id != ADMIN:
        return

    text = command.args

    user_ids = await a.get_all_user_ids()
    
    for user in user_ids:
        await bot.send_message(chat_id=user, text=text)