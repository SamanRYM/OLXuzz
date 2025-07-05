from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("8015835865:AAGQl9PWXc1t-Jm0PoQy4hY0_9x3oJJ9kfg")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📱 Добро пожаловать в OLXuz!\n\n🛒 Здесь вы можете найти и продать товары прямо в Telegram.",
        parse_mode="Markdown"
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
