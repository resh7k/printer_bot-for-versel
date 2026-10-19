# Printer Bot

Телеграм-бот на `aiogram` для работы с принтерами и картриджами.

## 📋 Требования

- Python 3.10+ (рекомендуется 3.13)
- Токен бота от [@BotFather](https://t.me/BotFather)

## 🚀 Установка и запуск

### 1. Клонирование репозитория
```bash
git clone https://github.com/resh7k/printer_bot.git
cd printer_bot
```


### 2. Создание виртуального окружения

powershell
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
Windows (CMD):
```
cmd
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
Linux / macOS:
```
bash
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Установка зависимостей
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Настройка переменных окружения
Создай файл .env в корне проекта (рядом с bot.py) и добавь туда свой токен:

env
```
BOT_TOKEN=твой_токен_от_BotFather
Важно: Файл .env не должен попадать в Git. Он уже добавлен в .gitignore.
```

### 5. Запуск бота
```bash
python bot.py
Если бот запустился успешно, в консоли появится:
```

```text
INFO:root:Бот запускается...
INFO:aiogram.dispatcher:Start polling
```

## 📁 Структура проекта

```text
printer_bot/
├── .env                  # Секреты (НЕ коммитится)
├── .env.example          # Шаблон для .env
├── .gitignore            # Игнорируемые файлы
├── requirements.txt      # Зависимости
├── bot.py                # Точка входа
├── config/               # Настройки
├── data/                 # Данные (JSON-файлы)
├── handlers/             # Обработчики команд и сообщений
├── img/                  # Изображения
├── keyboards/            # Клавиатуры
├── services/             # Бизнес-логика
├── states/               # FSM-состояния
└── webapp/               # Веб-приложение (мини-апп)
```

## 🛠 Технологии
aiogram 3.x — асинхронный фреймворк для Telegram Bot API
python-dotenv — загрузка переменных окружения из .env