from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from config.settings import FORM_URL, REFILL_URL
from keyboards.cities import get_cities_keyboard
from services.address_service import get_refill_addresses

router = Router()


# ============ СТАРТ ============


@router.message(F.text == "💧 Заправка картриджа")
async def refill_start(message: Message):
    """Клиент нажал «Заправка картриджа»."""
    await message.answer(
        text=("💧 <b>Заправка картриджа</b>\n\n" "Знаете модель картриджа?"),
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="✅ Да, знаю", callback_data="refill_yes")],
                [
                    InlineKeyboardButton(
                        text="❌ Нет, не знаю", callback_data="refill_no"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="📍 Наши адреса заправки",
                        callback_data="refill_addresses",
                    )
                ],
            ]
        ),
    )


# ============ АДРЕСА ============


@router.callback_query(F.data == "refill_addresses")
async def refill_addresses(callback: CallbackQuery):
    """Клиент нажал «Наши адреса заправки»."""
    await callback.message.edit_text(
        text="Выберите город:",
        reply_markup=get_cities_keyboard("refill"),
    )
    await callback.answer()


@router.callback_query(F.data.startswith("refill_city_"))
async def refill_city_selected(callback: CallbackQuery):
    """Клиент выбрал город для заправки."""
    city = callback.data.replace("refill_city_", "")
    data = get_refill_addresses(city)

    text = f"📍 {city}\n\n"
    for addr in data["main"]:
        text += f"• {addr['address']}\n"
        text += f"  🕐 {addr['hours']}\n"
        for phone in addr.get("phones", []):
            text += f"  📞 {phone}\n"
        text += "\n"

    # Партнёры (только у Пензы)
    if data.get("partners"):
        text += "Адреса наших партнёров:\n"
        for p in data["partners"]:
            text += f"• {p['address']}\n"

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


# ============ НЕТ, НЕ ЗНАЮ ============


@router.callback_query(F.data == "refill_no")
async def refill_no(callback: CallbackQuery, state: FSMContext):
    """Клиент не знает модель → ссылка на форму."""
    await callback.message.delete()

    await callback.message.answer(
        text=(
            "<b>Не проблема!</b>\n\n"
            "Разберёмся вместе — оставьте заявку,\n"
            "менеджер перезвонит в течение 15 минут."
        ),
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="🌐 Оставить заявку на сайте",
                        url=FORM_URL,
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="ℹ️ Главное меню", callback_data="back_to_start"
                    )
                ],
            ]
        ),
    )
    await callback.answer()


# ============ ДА, ЗНАЮ ============


@router.callback_query(F.data == "refill_yes")
async def refill_yes(callback: CallbackQuery, state: FSMContext):
    """Клиент знает модель → ссылка на сайт."""
    await callback.message.delete()

    await callback.message.answer(
        text=(
            "Выберите на сайте модель вашего картриджа, узнайте цену заправки и <b>оставьте заявку</b>\n\n"
            "Наш специалист перезвонит Вам и картридж будет заправлен!"
        ),
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="🌐 Оставить заявку на сайте",
                        url=REFILL_URL,
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="ℹ️ Главное меню", callback_data="back_to_start"
                    )
                ],
            ]
        ),
    )
    await callback.answer()
