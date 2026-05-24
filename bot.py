from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8971545585:AAE-5zg03r0ueBmj1bG4UKxxZGRpsuYktiA"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("🎭 Natok", callback_data="natok")],
        [InlineKeyboardButton("🎬 Movie", callback_data="movie")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🔥 Welcome To Gaming Live Bot 🔥",
        reply_markup=reply_markup
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "natok":

        await query.message.reply_text("🎭 Natok Video আসবে এখানে")

    elif query.data == "movie":

        await query.message.reply_text("🎬 Movie Video আসবে এখানে")


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(CallbackQueryHandler(button))

print("Bot Running...")

app.run_polling()