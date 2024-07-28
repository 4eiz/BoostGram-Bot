import asyncio

from aiocryptopay import AioCryptoPay
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from aiocryptopay import AioCryptoPay, Networks

from keyboards import client as k
from config import bot, CRYPTO_TOKEN
from app.fsm import CryproBot
from data import users as u
from app.ban_check import handle_blocked_user

router = Router()





@router.message(CryproBot.sum)
async def show(message: Message, state: FSMContext):

    amount = float(message.text.replace(',', '.'))

    text = '''<b>⏳ 🔹 Перейдите по ссылке из кнопки для оплаты!

🔄 После успешной оплаты, средства автоматически поступят на ваш баланс. </b>'''


    crypto = AioCryptoPay(token=CRYPTO_TOKEN, network=Networks.MAIN_NET)
    invoice = await crypto.create_invoice(amount=amount, fiat='RUB', currency_type='fiat')
    mes_rep = await message.answer(text, reply_markup=k.repl_kb(url=invoice.bot_invoice_url))
    
    
    await state.update_data(id=invoice.invoice_id)

    timeout = 60 * 5  # 60 минут
    interval = 5

    while timeout > 0:

        # Проверяем статус платежа
        print('Ошибка payment_status')
        payment_status = await check_crypto_bot_invoice(invoice.invoice_id)

        if payment_status == True:
            user_id = message.from_user.id
            
            await u.update_balance(user_id, amount)
            # Платеж выполнен, выполните соответствующие действия

            text_success = f'Баланс пополнен на {amount}'

            await message.answer(text_success)

            await bot.delete_message(chat_id=message.chat.id, message_id=mes_rep.message_id)
            break
        else:
            # Платеж не выполнен, уменьшаем таймаут
            timeout -= interval

        await asyncio.sleep(interval)
            

    if timeout <= 0:
        # Таймаут истек, отменяем платеж и отправляем сообщение об отмене
        await bot.delete_message(chat_id=message.chat.id, message_id=mes_rep.message_id)
        await crypto.delete_invoice(invoice_id=invoice.invoice_id)

    await state.clear()


@router.callback_query(k.Menu_callback.filter(F.menu == 'cancel_invoice'), CryproBot.sum)
async def cancel_repl(call: CallbackQuery, callback_data: k.Menu_callback, state: FSMContext):

    if await handle_blocked_user(call=call):
        return
    
    data = await state.get_data()
    invoice = data.get('id')
    status = await cancel_invoice(invoice=invoice)
    if status == True:
        text = 'Платёж отменён'
        await call.message.answer(text=text)
        await state.clear()
    else:
        await state.clear()



#-----------------------------


async def check_crypto_bot_invoice(invoice_id: int):
    cryptopay = AioCryptoPay(CRYPTO_TOKEN)
    invoice = await cryptopay.get_invoices(invoice_ids=invoice_id)
    await cryptopay.close()
    if invoice.status == 'paid':
        return True
    else:
        return False



async def cancel_invoice(invoice):

    try:
        crypto = AioCryptoPay(token=CRYPTO_TOKEN, network=Networks.MAIN_NET)

        await crypto.delete_invoice(invoice_id=invoice)
        return True
    except Exception as e:
        print(e)
        return False