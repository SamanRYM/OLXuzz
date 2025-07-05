from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ❗ Временно вставленный токен (заменим на os.getenv позже)
TOKEN = "8015835865:AAGQl9PWXc1t-Jm0PoQy4hY0_9x3oJJ9kfg"

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Добро пожаловать в бота OLXuz!\n\n"
        "🛍 Здесь вы можете быстро перейти на сайт OLX.uz и найти всё, что нужно:\n"
        "📱 Телефоны, 💻 ноутбуки, 📺 техника, 🛒 товары и многое другое!\n\n"
        "🚀 Быстро, удобно и прямо внутри Telegram — без регистрации и лишних шагов.\n\n"
        "👉 Просто нажмите кнопку в меню или используйте WebApp, чтобы начать покупки!"
    )

# Запуск бота
if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
