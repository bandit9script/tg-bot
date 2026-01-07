from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🛒 Купить SeilWare", callback_data="buy"),
            InlineKeyboardButton("📄 Описание", callback_data="desc")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Выбери действие:",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "buy":
        await query.message.reply_text(
            "Привет, вот он 👉 @DollarWare\n"
            "Ты можешь купить SeilWare по низкой цене"
        )

    elif query.data == "desc":
        await query.message.reply_text(
            "При покупке мы даём вам гарантию на неделю\n"
            "Поддержка: @Ragfa9"
        )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.run_polling()

if __name__ == "__main__":
    main()
