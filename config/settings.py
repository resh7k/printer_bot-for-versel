import os

from dotenv import load_dotenv

# Загружаем .env
load_dotenv()

# Читаем переменные
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID"))
CATALOG_URL = os.getenv("CATALOG_URL")
REPAIR_URL = os.getenv("REPAIR_URL")
REFILL_URL = os.getenv("REFILL_URL")
FORM_URL = os.getenv("FORM_URL")

# Проверка, что всё на месте
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден в .env")

if not ADMIN_CHAT_ID:
    raise ValueError("ADMIN_CHAT_ID не найден в .env")

if not CATALOG_URL:
    raise ValueError("CATALOG_URL не найден в .env")

WEBAPP_URL = "https://resh7k.github.io/printer-bot_/"
