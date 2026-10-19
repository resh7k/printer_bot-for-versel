# api/index.py
from fastapi import FastAPI, Request

from bot import bot, dp  # Импортируем наш диспетчер и бота из bot.py
from config.settings import BOT_TOKEN

app = FastAPI()


@app.post("/api/webhook")
async def telegram_webhook(request: Request):
    """Принимает обновления от Telegram и передает их в диспетчер."""
    update_data = await request.json()
    # Передаем апдейт в aiogram
    await dp.feed_raw_update(bot, update_data)
    return {"ok": True}
