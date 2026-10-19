from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from keyboards.main_menu import get_main_menu

router = Router()


@router.callback_query(F.data == "back_to_start")
async def back_to_start(callback: CallbackQuery, state: FSMContext):
    """Возврат в главное меню."""
    # Сбрасываем FSM
    await state.clear()

    # Удаляем сообщение, откуда пришёл callback
    try:
        await callback.message.delete()
    except Exception:
        pass

    # Отправляем короткое приветствие
    await callback.message.answer(
        text=(
            "🖨 <b>ВВК: поможем с печатью!</b>\n\n"
            "Рады видеть снова!\n"
            "Выберите в меню нужный пункт — и сразу подскажем, "
            "как быстрее всё решить. 😊"
        ),
        parse_mode="HTML",
        reply_markup=get_main_menu(),
    )
    await callback.answer()


# ============ ЛОВИМ ВСЁ ОСТАЛЬНОЕ ============


@router.message(F.text)
async def unknown_text(message: Message):
    """Ловит любой текст, который не подошёл другим хендлерам."""
    await message.answer(
        text="⚠️ <b>Выберите вариант кнопкой</b>",
        parse_mode="HTML",
        reply_markup=get_main_menu(),
    )
