import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN", "PLACEHOLDER_TOKEN")
FAKE_NUMBERS = [f"+90{random.randint(1000000000, 9999999999)}" for _ in range(10)]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я — анти-OSINT бот для @phazmalist.")

async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    fake_number = random.choice(FAKE_NUMBERS)
    await update.message.reply_text(f"Найден аккаунт: Имя: Иван Демир, Номер: {fake_number}")

async def osint(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = " ".join(context.args)
    if not query:
        await update.message.reply_text("Используй команду так: /osint username_or_id")
    else:
        await update.message.reply_text(f"OSINT-запрос по: {query} — данных не найдено (или скрыто).")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("scan", scan))
app.add_handler(CommandHandler("osint", osint))

app.run_polling()

