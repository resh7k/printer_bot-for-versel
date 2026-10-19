from aiogram import F, Router
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from config.settings import CATALOG_URL
from keyboards.buy_kb import get_buy_menu
from keyboards.cities import get_cities_keyboard
from services.address_service import get_buy_addresses

router = Router()


@router.message(F.text == "🖨 Купить принтер")
async def buy_start(message: Message):
    """Клиент нажал «Купить принтер»."""
    await message.answer(
        text=(
            "У нас есть каталог доступных\n"
            "лазерных принтеров и МФУ.\n\n"
            "Посмотрите модели, фильтры и цены."
        ),
        reply_markup=get_buy_menu(CATALOG_URL),
    )


@router.callback_query(F.data == "buy_offline")
async def buy_offline(callback: CallbackQuery):
    """Клиент нажал «Купить оффлайн»."""
    await callback.message.edit_text(
        text="Выберите город:",
        reply_markup=get_cities_keyboard("buy"),
    )
    await callback.answer()


@router.callback_query(F.data.startswith("buy_city_"))
async def buy_city_selected(callback: CallbackQuery):
    """Клиент выбрал город."""
    city = callback.data.replace("buy_city_", "")
    data = get_buy_addresses(city)

    # Формируем текст
    text = f"📍 {city}\n\n"
    for addr in data["main"]:
        text += f"• {addr['address']}\n"
        text += f"  🕐 {addr['hours']}\n"
        for phone in addr.get("phones", []):
            text += f"  📞 {phone}\n"
        text += "\n"

    # Кнопки
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
