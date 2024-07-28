import asyncio
import logging
from aiogram import Dispatcher


from app import general, profile, coupon
from app.buy_boost import tg_subs, buy_boost, tg_prem_subs, tg_views, tg_boost, tg_prem_views, tg_reactions, order, tg_prem_start_bot
from app.replenishment import replenish, cb
from app.admin import remote_services, remote_coupons, remote_users, newsletter
from config import bot




async def start():
    dp = Dispatcher()

    dp.include_routers(
        general.router,
        buy_boost.router,
        tg_subs.router,
        tg_prem_subs.router,
        tg_views.router,
        tg_boost.router,
        tg_prem_views.router,
        tg_reactions.router,
        profile.router,
        order.router,
        replenish.router,
        cb.router,
        remote_services.router,
        remote_coupons.router,
        coupon.router,
        remote_users.router,
        tg_prem_start_bot.router,
        newsletter.router,
    )

    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(start())
