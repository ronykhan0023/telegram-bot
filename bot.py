from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

# তোমার নতুন Bot Token এখানে বসাও
TOKEN = "8971545585:AAE-5zg03r0ueBmj1bG4UKxxZGRpsuYktiA"


# ================= START COMMAND =================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("🎭 Natok", callback_data="natok")],
        [InlineKeyboardButton("🎬 Movie", callback_data="movie")],
        [InlineKeyboardButton("😁 Collection", callback_data="collection")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🎬 Welcome To Video Collection 🎬\n\nনিচের অপশন সিলেক্ট করুন 👇",
        reply_markup=reply_markup
    )


# ================= BUTTON SYSTEM =================

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    # Natok Button
    if query.data == "natok":

        await query.message.reply_text(
            "🎭 Natok Video আসবে এখানে"
        )

    # Movie Button
    elif query.data == "movie":

        await query.message.reply_text(
            "🎬 Movie Video আসবে এখানে"
        )

    # Collection Button
    elif query.data == "collection":

        await query.message.reply_text(
            "😁 Collection জিনিস আসবে এখানে"
        )


# ================= MAIN =================

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(CallbackQueryHandler(button))

print("✅ Bot Running...")

app.run_polling()
