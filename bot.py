import logging

from aiogram import Bot, Dispatcher

from config.settings import BOT_TOKEN
from handlers import buy, common, question, refill, repair, start

# Логирование
logging.basicConfig(level=logging.INFO)

# Создаём бота и диспетчер
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Подключаем роутеры (common — ВСЕГДА последним!)
dp.include_router(start.router)
dp.include_router(buy.router)
dp.include_router(repair.router)
dp.include_router(refill.router)
dp.include_router(question.router)
dp.include_router(common.router)
