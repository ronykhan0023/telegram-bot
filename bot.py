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
#                    BOT TOKEN
# =====================================================

TOKEN = "8971545585:AAE-5zg03r0ueBmj1bG4UKxxZGRpsuYktiA"


# =====================================================
#                TELEGRAM VIDEO FILE IDs
# =====================================================

# 🎭 Natok Videos
NATOK_1 = "PUT_NATOK_FILE_ID"

# 🎬 Movie Videos
MOVIE_1 = "PUT_MOVIE_FILE_ID"

# 😁 Collection Videos
COLLECTION_1 = "PUT_COLLECTION_FILE_ID"


# =====================================================
#                    START COMMAND
# =====================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [

        [InlineKeyboardButton("🎭 Natok", callback_data="natok")],

        [InlineKeyboardButton("🎬 Movie", callback_data="movie")],

        [InlineKeyboardButton("😁 Collection", callback_data="collection")],

        [InlineKeyboardButton("📺 Web Series", callback_data="series")],

        [InlineKeyboardButton("🔥 Trending", callback_data="trending")],

        [InlineKeyboardButton("😂 Funny Clips", callback_data="funny")]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_text = """
🎬 Welcome To Video Collection 🎬

📁 সকল ধরনের ভিডিও এখানে পাবেন।

👇 নিচের অপশন থেকে সিলেক্ট করুন
"""

    await update.message.reply_text(
        welcome_text,
        reply_markup=reply_markup
    )


# =====================================================
#                  BUTTON SYSTEM
# =====================================================

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    # ==========================================
    # Natok
    # ==========================================

    if query.data == "natok":

        await query.message.reply_video(
            video=NATOK_1,
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
            video=MOVIE_1,
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
            video=COLLECTION_1,
            caption="""
😁 Video Collection

✅ Viral Videos
✅ Social Clips
✅ Short Videos
"""
        )

    # ==========================================
    # Web Series
    # ==========================================

    elif query.data == "series":

        await query.message.reply_text(
            """
📺 Web Series Collection

🔥 Coming Soon...
"""
        )

    # ==========================================
    # Trending
    # ==========================================

    elif query.data == "trending":

        await query.message.reply_text(
            """
🔥 Trending Videos

🚀 Coming Soon...
"""
        )

    # ==========================================
    # Funny Clips
    # ==========================================

    elif query.data == "funny":

        await query.message.reply_text(
            """
😂 Funny Clips

🤣 Coming Soon...
"""
        )


# =====================================================
#               FILE ID GET SYSTEM
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
#                     MAIN SYSTEM
# =====================================================

app = Application.builder().token(TOKEN).build()

# Start Command
app.add_handler(CommandHandler("start", start))

# Button System
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
