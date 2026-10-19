from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_main_menu() -> ReplyKeyboardMarkup:
    """Главное меню бота."""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📝 Заказать картриджи")],
            [KeyboardButton(text="🖨 Купить принтер")],
            [KeyboardButton(text="⚙️ Ремонт принтера")],
            [KeyboardButton(text="💧 Заправка картриджа")],
            [KeyboardButton(text="💬 Другой вопрос")],
        ],
        resize_keyboard=True,
    )
    return keyboard
