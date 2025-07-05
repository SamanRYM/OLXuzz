from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ⚠️ Токен вставлен напрямую (НЕБЕЗОПАСНО — только для теста!)
TOKEN = "8015835865:AAGQl9PWXc1t-Jm0PoQy4hY0_9x3oJJ9kfg"

# Функция при /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📱 Добро пожаловать в OLXuz!\nНайдите товары быстро и удобно!")

# Запуск бота
if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
