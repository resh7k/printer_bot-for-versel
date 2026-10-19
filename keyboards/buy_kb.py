from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_buy_menu(catalog_url: str) -> InlineKeyboardMarkup:
    """Меню ветки «Купить принтер»."""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🌐 Перейти на сайт",
                    url=catalog_url,
                )
            ],
            [
                InlineKeyboardButton(
                    text="🏬 Купить оффлайн",
                    callback_data="buy_offline",
                )
            ],
        ]
    )
    return keyboard
