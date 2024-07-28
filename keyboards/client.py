from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters.callback_data import CallbackData
from config import CHANNEL_URL, SUPPORT_URL




class Menu_callback(CallbackData, prefix="menu"):
    menu: str

class Buy_info(CallbackData, prefix="boost"):
    menu: str
    service: int



def menu_kb():
    kb = [
        [
            InlineKeyboardButton(text='🌐 Заказать накрутку', callback_data=Menu_callback(menu="buy_boost").pack()),
        ],
        [
            InlineKeyboardButton(text='👤 Профиль', callback_data=Menu_callback(menu="profile").pack()),
            InlineKeyboardButton(text='📫 Канал', url=CHANNEL_URL),
        ],
        [
            InlineKeyboardButton(text='🛠️ Поддержка', url=SUPPORT_URL),
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=kb)


def profile_kb():
    kb = [
        [
            InlineKeyboardButton(text='💸 Пополнить баланс', callback_data=Menu_callback(menu="replenish").pack()),
        ],
        [
            InlineKeyboardButton(text='Активировать купон', callback_data=Menu_callback(menu="coupon").pack())
        ],
        [
            InlineKeyboardButton(text='Главное меню', callback_data=Menu_callback(menu="menu").pack())
        ],
    ]

    return InlineKeyboardMarkup(inline_keyboard=kb)


def replenishment_kb():
    kb = [
        [
            InlineKeyboardButton(text='Cryptobot', callback_data=Menu_callback(menu="cryptobot").pack()),
        ],
        # [
        #     InlineKeyboardButton(text='AAIO', callback_data=Menu_callback(menu="aaio").pack())
        # ],
    ]

    return InlineKeyboardMarkup(inline_keyboard=kb)


def support_kb():
    kb = [
        [
            InlineKeyboardButton(text='🛠️ Поддержка', url=SUPPORT_URL),
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=kb)


def category_kb():
    kb = [
        [
            InlineKeyboardButton(text='Телеграм подписчики/участники', callback_data=Menu_callback(menu="tg_subs").pack()),
        ],
        [
            InlineKeyboardButton(text='Телеграм премиум подписчики/участники', callback_data=Menu_callback(menu="tg_prem_subs").pack()),
        ],
        [
            InlineKeyboardButton(text='Просмотры', callback_data=Menu_callback(menu="tg_views").pack()),
            InlineKeyboardButton(text='Премиум просмотры', callback_data=Menu_callback(menu="tg_prem_views").pack()),
        ],
        [
            InlineKeyboardButton(text='Премиум Start Bot', callback_data=Menu_callback(menu="tg_prem_start_bot").pack()),
        ],
        [
            InlineKeyboardButton(text='Реакции', callback_data=Menu_callback(menu="tg_reactions").pack()),
            InlineKeyboardButton(text='Телеграм BOOST', callback_data=Menu_callback(menu="tg_boost").pack()),
        ],
        [
            InlineKeyboardButton(text='Главное меню', callback_data=Menu_callback(menu="menu").pack()),
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=kb)


def tg_subs_kb():
    kb = [
        [
            InlineKeyboardButton(text='Подписчики/участники 3 дня гарантии', callback_data=Buy_info(menu="tg_subs", service=19).pack()),
        ],
        [
            InlineKeyboardButton(text='Подписчики/участники 7 дней гарантии', callback_data=Buy_info(menu="tg_subs", service=20).pack()),
        ],
        [
            InlineKeyboardButton(text='Подписчики/участники 30 дней гарантии', callback_data=Buy_info(menu="tg_subs", service=21).pack()),
        ],
        [
            InlineKeyboardButton(text='Подписчики/участники Вечные', callback_data=Buy_info(menu="tg_subs", service=55).pack()),
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data=Menu_callback(menu="buy_boost").pack()),
        ],
    ]

    return InlineKeyboardMarkup(inline_keyboard=kb)


def tg_prem_subs_kb():
    kb = [
        [
            InlineKeyboardButton(text='Премиум п/у | 3-7 дней гарантии', callback_data=Buy_info(menu="tg_prem_subs", service=79).pack()),
        ],
        [
            InlineKeyboardButton(text='Премиум п/у | 7-10 дней гарантии', callback_data=Buy_info(menu="tg_prem_subs", service=78).pack()),
        ],
        [
            InlineKeyboardButton(text='Премиум п/у | 10-14 дней гарантии', callback_data=Buy_info(menu="tg_prem_subs", service=75).pack()),
        ],
        [
            InlineKeyboardButton(text='Премиум п/у | 14-20 дней гарантии', callback_data=Buy_info(menu="tg_prem_subs", service=112).pack()),
        ],
        [
            InlineKeyboardButton(text='Премиум п/у | 20-30 дней гарантии', callback_data=Buy_info(menu="tg_prem_subs", service=107).pack()),
        ],
        [
            InlineKeyboardButton(text='Ru Премиум п/у | 7-14 дней гарантии', callback_data=Buy_info(menu="tg_prem_subs", service=84).pack()),
        ],
        [
            InlineKeyboardButton(text='Ru Премиум п/у | 15-30 дней гарантии', callback_data=Buy_info(menu="tg_prem_subs", service=85).pack()),
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data=Menu_callback(menu="buy_boost").pack()),
        ],
    ]

    return InlineKeyboardMarkup(inline_keyboard=kb)


def tg_views_kb():
    kb = [
        [
            InlineKeyboardButton(text='Посмотры Ru', callback_data=Buy_info(menu="tg_views", service=96).pack()),
        ],
        [
            InlineKeyboardButton(text='Посмотры Mix', callback_data=Buy_info(menu="tg_views", service=95).pack()),
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data=Menu_callback(menu="buy_boost").pack()),
        ],
    ]

    return InlineKeyboardMarkup(inline_keyboard=kb)


def tg_prem_views_kb():
    kb = [
        [
            InlineKeyboardButton(text='Ru Премиум просмотры', callback_data=Buy_info(menu="tg_prem_views", service=91).pack()),
        ],
        [
            InlineKeyboardButton(text='Mix Премиум просмотры', callback_data=Buy_info(menu="tg_prem_views", service=90).pack()),
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data=Menu_callback(menu="buy_boost").pack()),
        ],
    ]

    return InlineKeyboardMarkup(inline_keyboard=kb)


def tg_reactions_kb():
    kb = [
        [
            InlineKeyboardButton(text='Положительные реакции', callback_data=Buy_info(menu="tg_reactions", service=29).pack()),
        ],
        [
            InlineKeyboardButton(text='Негативные реакции', callback_data=Buy_info(menu="tg_reactions", service=37).pack()),
        ],
        [
            InlineKeyboardButton(text='Премиум положительные реакции', callback_data=Buy_info(menu="tg_reactions", service=81).pack()),
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data=Menu_callback(menu="buy_boost").pack()),
        ],
    ]

    return InlineKeyboardMarkup(inline_keyboard=kb)


def tg_boosts():
    kb = [
        [
            InlineKeyboardButton(text='BOOST частные и открытые каналы | гарантия 1-7 дней', callback_data=Buy_info(menu="tg_boost", service=77).pack()),
        ],
        [
            InlineKeyboardButton(text='BOOST частные и открытые каналы | гарантия 30 дней', callback_data=Buy_info(menu="tg_boost", service=72).pack()),
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data=Menu_callback(menu="buy_boost").pack()),
        ],
    ]

    return InlineKeyboardMarkup(inline_keyboard=kb)


def tg_prem_start():
    kb = [
        [
            InlineKeyboardButton(text='Premium BOT START | 7-14 ДНЕЙ | БЕЗ ОТПИСОК', callback_data=Buy_info(menu="tg_prem_start_bot", service=80).pack()),
        ],
        [
            InlineKeyboardButton(text='Premium BOT START | 15-30 ДНЕЙ БЕЗ ОТПИСОК', callback_data=Buy_info(menu="tg_prem_start_bot", service=86).pack()),
        ],
        [
            InlineKeyboardButton(text='RU Premium BOT START | 7-14 ДНЕЙ', callback_data=Buy_info(menu="tg_prem_start_bot", service=87).pack()),
        ],
        [
            InlineKeyboardButton(text='RU Premium BOT START | 15-30 DAYS NO DROP', callback_data=Buy_info(menu="tg_prem_start_bot", service=88).pack()),
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data=Menu_callback(menu="buy_boost").pack()),
        ],
    ]

    return InlineKeyboardMarkup(inline_keyboard=kb)


def order_kb(menu, service):
    kb = [
        [
            InlineKeyboardButton(text='Заказать', callback_data=Buy_info(menu="order", service=service).pack()),
        ],
        [
            InlineKeyboardButton(text='Отмена', callback_data=Menu_callback(menu=menu).pack()),
        ],
    ]

    return InlineKeyboardMarkup(inline_keyboard=kb)


def conf_kb():
    kb = [
        [
            InlineKeyboardButton(text='Подтвердить', callback_data=Menu_callback(menu='confirmation').pack()),
        ],
        [
            InlineKeyboardButton(text='Отмена', callback_data=Menu_callback(menu='buy_boost').pack()),
        ],
    ]

    return InlineKeyboardMarkup(inline_keyboard=kb)


def cancel_kb():
    kb = [
        [
            InlineKeyboardButton(text='Отмена', callback_data=Menu_callback(menu='buy_boost').pack()),
        ],
    ]

    return InlineKeyboardMarkup(inline_keyboard=kb)


def repl_kb(url):
    kb = [
        [
            InlineKeyboardButton(text='ОПЛАТИТЬ', url=url)
        ],
        [
            InlineKeyboardButton(text='Отмена', callback_data=Menu_callback(menu="cancel_invoice").pack())
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)