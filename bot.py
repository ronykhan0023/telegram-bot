from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
    ContextTypes
)

# =====================================================
#                     BOT TOKEN
# =====================================================

TOKEN = "8971545585:AAE-5zg03r0ueBmj1bG4UKxxZGRpsuYktiA"


# =====================================================
#               YOUR TELEGRAM FILE IDs
# =====================================================

# 🎭 Natok Video
NATOK_VIDEO = "PUT_NATOK_FILE_ID"

# 🎬 Movie Video
MOVIE_VIDEO = "PUT_MOVIE_FILE_ID"

# 😁 Collection Video
COLLECTION_VIDEO = "PUT_COLLECTION_FILE_ID"


# =====================================================
#                    START COMMAND
# =====================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [

        [InlineKeyboardButton("🎭 Natok", callback_data="natok")],

        [InlineKeyboardButton("🎬 Movie", callback_data="movie")],

        [InlineKeyboardButton("😁 Collection", callback_data="collection")]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    text = """
🎬 Welcome To Video Collection 🎬

📁 এখানে সকল ধরনের ভিডিও পাবেন।

👇 নিচের অপশন সিলেক্ট করুন
"""

    await update.message.reply_text(
        text,
        reply_markup=reply_markup
    )


# =====================================================
#                    BUTTON SYSTEM
# =====================================================

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    # ==========================================
    # Natok
    # ==========================================

    if query.data == "natok":

        await query.message.reply_video(
            video=NATOK_VIDEO,
            caption="""
🎭 Natok Collection

✅ Bangla Natok
✅ Romantic Natok
✅ Funny Natok
"""
        )

    # ==========================================
    # Movie
    # ==========================================

    elif query.data == "movie":

        await query.message.reply_video(
            video=MOVIE_VIDEO,
            caption="""
🎬 Movie Collection

✅ Bangla Movie
✅ Hindi Movie
✅ English Movie
"""
        )

    # ==========================================
    # Collection
    # ==========================================

    elif query.data == "collection":

        await query.message.reply_video(
            video=COLLECTION_VIDEO,
            caption="""
😁 Collection Videos

✅ Viral Videos
✅ Funny Clips
✅ Trending Videos
"""
        )


# =====================================================
#                 FILE ID GETTER SYSTEM
# =====================================================

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # Video File ID
    if update.message.video:

        file_id = update.message.video.file_id

        await update.message.reply_text(
            f"""
🎬 YOUR VIDEO FILE ID 👇

{file_id}
"""
        )

    # Document File ID
    elif update.message.document:

        file_id = update.message.document.file_id

        await update.message.reply_text(
            f"""
📁 YOUR FILE ID 👇

{file_id}
"""
        )


# =====================================================
#                      MAIN
# =====================================================

app = Application.builder().token(TOKEN).build()

# Start Command
app.add_handler(CommandHandler("start", start))

# Button Click System
app.add_handler(CallbackQueryHandler(button))

# File ID Getter
app.add_handler(
    MessageHandler(
        filters.VIDEO | filters.Document.ALL,
        get_file_id
    )
)

print("✅ Video Collection Bot Running...")

app.run_polling()
