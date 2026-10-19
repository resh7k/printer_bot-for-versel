import json
from datetime import datetime

from aiogram import Bot, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from config.settings import ADMIN_CHAT_ID

router = Router()

TYPE_TITLES = {
    "refill": "Заправка",
    "repair": "Ремонт",
}


@router.message(F.web_app_data)
async def handle_webapp_data(message: Message, bot: Bot, state: FSMContext):
    """Ловит данные из Mini App и шлёт в группу."""
    try:
        data = json.loads(message.web_app_data.data)
    except json.JSONDecodeError:
        await message.answer("Ошибка: не удалось прочитать данные.")
        return

    type_key = data.get("type", "refill")
    type_title = TYPE_TITLES.get(type_key, "Заявка")

    lines = [f"🔔 НОВАЯ ЗАЯВКА — {type_title}", ""]

    if type_key == "refill" and data.get("brand"):
        lines.append(f"🖨 Бренд: {data.get('brand', '—')}")
        lines.append(f"🖨 Модель: {data.get('model', '—')}")
        lines.append(f"💧 Картридж: {data.get('cartridge', '—')}")

        refill = data.get("refill_price", 0)
        replace = data.get("replace_price", 0)

        refill_text = f"{refill}₽" if refill > 0 else "нет в наличии"
        replace_text = f"{replace}₽" if replace > 0 else "нет в наличии"

        lines.append(f"💰 Заправка: {refill_text}")
        lines.append(f"💰 Замена: {replace_text}")
        lines.append("")

    lines.append(f"👤 Имя: {data.get('name', '—')}")
    lines.append(f"📞 Телефон: {data.get('phone', '—')}")
    lines.append("")
    lines.append(f"🕐 {datetime.now().strftime('%d.%m.%Y %H:%M')}")
    lines.append(
        f"👤 @{message.from_user.username or '—'} (ID: {message.from_user.id})"
    )

    text = "\n".join(lines)

    # Отправляем в группу
    try:
        await bot.send_message(chat_id=ADMIN_CHAT_ID, text=text)
    except Exception as e:
        await message.answer(f"Ошибка отправки в группу: {e}")
        return

    # Убираем inline-кнопку у предыдущего сообщения («Вернёмся в меню?»)
    state_data = await state.get_data()
    prompt_message_id = state_data.get("prompt_message_id")
    if prompt_message_id:
        try:
            await bot.edit_message_reply_markup(
                chat_id=message.chat.id,
                message_id=prompt_message_id,
                reply_markup=None,
            )
        except Exception:
            pass  # если не получилось — не падаем

    # Отвечаем клиенту + inline-кнопка «ℹ️ Главное меню»
    await message.answer(
        "✅ Заявка принята!\n" "Мы свяжемся с вами в течение 15 минут.",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="ℹ️ Главное меню", callback_data="back_to_start"
                    )
                ]
            ]
        ),
    )

    # Сбрасываем FSM
    await state.clear()
