from aiogram import F, Router
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from config.settings import FORM_URL

router = Router()


@router.message(F.text == "💬 Другой вопрос")
async def question_start(message: Message):
    """Клиент нажал «Другой вопрос»."""
    await message.answer(
        text=(
            "<b>Задайте нам любой вопрос</b>\n\n"
            "Менеджер ответит в течении <b>15 минут</b>"
        ),
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="🌐 Задать вопрос",
                        url=FORM_URL,
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="ℹ️ Главное меню",
                        callback_data="back_to_start",
                    )
                ],
            ]
        ),
    )
