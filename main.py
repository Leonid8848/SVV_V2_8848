from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from flask import Flask
import threading

TOKEN = "8272083484:AAFVBArcF3HFtmNhqh1lRTfrMc6FQeXqvSY"

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я не твой бот 🤖")

# Эхо-ответ
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

# Фейковый Flask-сервер для Render
def run_flask():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return "Бот работает, Render не паникуй"

    app.run(host='0.0.0.0', port=10000)

# Главный блок
def main():
    # Запускаем Flask в фоне
    threading.Thread(target=run_flask).start()

    # Запускаем телеграм-бота
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("✅ Бот запущен")
    app.run_polling()

if __name__ == "__main__":
    main()
