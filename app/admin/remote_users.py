from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

from keyboards import client as k
from data import users as u

from config import bot, ADMIN
from app.ban_check import handle_blocked_user


router = Router()




@router.message(Command('ban'))
async def change_price(message: Message, command: CommandObject, state: FSMContext):

    user_id = command.args

    await u.update_ban_status(user_id, ban_status=1)


@router.message(Command('unban'))
async def change_price(message: Message, command: CommandObject, state: FSMContext):

    user_id = command.args

    await u.update_ban_status(user_id, ban_status=0)