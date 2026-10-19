from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from config.settings import FORM_URL
from keyboards.main_menu import get_main_menu

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    """Обработчик /start."""
    await state.clear()
    await message.answer(
        text=(
            "<b>Добро пожаловать в ВВК!</b> 🙋🏼‍♂️\n\n"
            "Мы знаем о печати все и чуть больше….!\n\n😉"
            "<b>Выберите в меню тот раздел, который вам интересен.</b>\n"
            "Если не нашли нужное, то нажмите  «Другой вопрос» и мы все решим…..🙂"
        ),
        parse_mode="HTML",
        reply_markup=get_main_menu(),
    )


# ============ ЗАКАЗАТЬ КАРТРИДЖ ============


@router.message(F.text == "📝 Заказать картриджи")
async def order_cartridge(message: Message):
    """Клиент нажал «Заказать картридж» → ссылка на сайт."""
    await message.answer(
        text=(
            "<b>✏️ Оставьте заявку</b> на нашем сайте\n\n"
            "Мы привезём вам полные картриджы \n"
            'по программе <b><i>"Вечный картридж"</i></b>'
        ),
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="🌐 Оставить заявку",
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
