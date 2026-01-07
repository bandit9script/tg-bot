import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# ================= KEEP ALIVE =================

class KeepAliveHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive")

def keep_alive():
    server = HTTPServer(("0.0.0.0", 8080), KeepAliveHandler)
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()

keep_alive()

# ================= BOT =================

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN not found in Secrets")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Купить SeilWare"],
        ["ОПИСАНИЕ"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Привет! Нажми кнопку ниже 👇",
        reply_markup=reply_markup
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "ОПИСАНИЕ":
        await update.message.reply_text(
            "При покупке мы даём вам гарантию на неделю\n@Ragfa9"
        )

    elif text == "Купить SeilWare":
        await update.message.reply_text(
            "Привет, вот он 👉 @DollarWare\n"
            "Ты можешь купить SeilWare по низкой цене"
        )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, buttons))

    print("Bot started")
    app.run_polling()

if __name__ == "__main__":
    main()