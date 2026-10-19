from aiogram import F, Router
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from config.settings import REPAIR_URL
from keyboards.cities import get_cities_keyboard
from services.address_service import get_repair_addresses

router = Router()


@router.message(F.text == "⚙️ Ремонт принтера")
async def repair_start(message: Message):
    """Клиент нажал «Ремонт принтера»."""
    # Сообщение 1 — БЕЗ reply-кнопки
    await message.answer(
        text=(
            "🖨️<b>Ремонт лазерного принтера</b>\n\n"
            "⚡ <b>Бесплатная диагностика</b> — <i>для Вас всегда</i>\n\n"
            "• Выезд мастера\n"
            "• Гарантия качества"
        ),
        parse_mode="HTML",
    )
    # Сообщение 2 + ТРИ inline-кнопки
    await message.answer(
        text=(
            "<b>Оставьте заявку</b> и менеджер перезвонит "
            "вам в течении <b>15 минут</b>\n\n"
            "Либо <b>выберете удобную мастерскую</b>\n"
            "<b>и звоните нам!</b> 👇"
        ),
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="🗺️ Посмотреть адреса",
                        callback_data="repair_addresses",
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="🌐 Оставить заявку на сайте",
                        url=REPAIR_URL,
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


@router.callback_query(F.data == "repair_addresses")
async def repair_addresses(callback: CallbackQuery):
    """Клиент нажал «Адреса ремонта»."""
    await callback.message.edit_text(
        text="Выберите город:",
        reply_markup=get_cities_keyboard("repair"),
    )
    await callback.answer()


@router.callback_query(F.data.startswith("repair_city_"))
async def repair_city_selected(callback: CallbackQuery):
    """Клиент выбрал город для ремонта."""
    city = callback.data.replace("repair_city_", "")
    data = get_repair_addresses(city)

    text = f"📍 {city}\n\n"
    for addr in data["main"]:
        text += f"• {addr['address']}\n"
        text += f"  🕐 {addr['hours']}\n"
        for phone in addr.get("phones", []):
            text += f"  📞 {phone}\n"
        text += "\n"

    buttons = []
    if data["map_link"]:
        buttons.append(
            [InlineKeyboardButton(text="🗺 Посмотреть на карте", url=data["map_link"])]
        )
    buttons.append(
        [InlineKeyboardButton(text="ℹ️ Главное меню", callback_data="back_to_start")]
    )

    await callback.message.edit_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons),
    )
    await callback.answer()
