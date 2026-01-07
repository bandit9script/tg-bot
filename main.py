from keep_alive import keep_alive

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.getenv("BOT_TOKEN")

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Купить SeilWare"],
        ["ОПИСАНИЕ"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard=False
    )

    await update.message.reply_text(
        "Нажми на кнопку 👇",
        reply_markup=reply_markup
    )

# обработка нажатий кнопок
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "ОПИСАНИЕ":
        await update.message.reply_text(
            "При покупке мы даём вам гарантию на неделю\n@Ragfa9"
        )

    elif text == "Купить SeilWare":
        await update.message.reply_text(
            "Привет!\nВот он 👉 @DollarWare\n"
            "Ты можешь купить SeilWare по низкой цене"
        )

def main():
    keep_alive()  # чтобы Replit не засыпал

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))

    print("Bot started")
    app.run_polling()

if __name__ == "__main__":
    main()
