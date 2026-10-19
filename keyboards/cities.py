from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from services.address_service import get_cities


def get_cities_keyboard(prefix: str) -> InlineKeyboardMarkup:
    """Клавиатура с городами. prefix — для callback_data (buy, refill, repair)."""
    cities = get_cities()

    # По 2 кнопки в ряд
    buttons = []
    row = []
    for city in cities:
        row.append(
            InlineKeyboardButton(
                text=city,
                callback_data=f"{prefix}_city_{city}",
            )
        )
        if len(row) == 2:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)

    # Кнопка «Назад» в главное меню — опционально
    buttons.append(
        [InlineKeyboardButton(text="ℹ️ Главное меню", callback_data="back_to_start")]
    )

    return InlineKeyboardMarkup(inline_keyboard=buttons)
