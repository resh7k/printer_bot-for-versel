from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo


def get_application_button(
    webapp_url: str,
    app_type: str = "refill",
    page: str = "index.html",
) -> ReplyKeyboardMarkup:
    """Reply-клавиатура с кнопкой Mini App.

    app_type: 'refill' или 'repair' — передаётся в URL как ?type=...
    page: какой HTML открывать — index.html или refill.html
    """
    url = f"{webapp_url}/{page}?type={app_type}"
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="📝 Оставить заявку",
                    web_app=WebAppInfo(url=url),
                )
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    return keyboard
