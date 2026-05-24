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

TOKEN = "8971545585:AAHNJGwWJbzgEofYTd5qEJ4CQBpjCXkbksg"


# =====================================================
#               TELEGRAM VIDEO FILE IDs
# =====================================================

# 🎭 Natok Video
NATOK_VIDEO_1 = "PUT_NATOK_FILE_ID"

# 🎬 Movie Video
MOVIE_VIDEO_1 = "PUT_MOVIE_FILE_ID"

# 😁 Collection Video
COLLECTION_VIDEO_1 = "PUT_COLLECTION_FILE_ID"

# 📺 Web Series
SERIES_VIDEO_1 = "PUT_SERIES_FILE_ID"

# 🔥 Trending
TRENDING_VIDEO_1 = "PUT_TRENDING_FILE_ID"

# 😂 Funny Clips
FUNNY_VIDEO_1 = "PUT_FUNNY_FILE_ID"


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

    text = """
🎬 Welcome To Video Collection 🎬

━━━━━━━━━━━━━━━━━━

🔥 Premium Video Collection Bot

✅ Natok
✅ Movie
✅ Funny Clips
✅ Trending Videos
✅ Web Series

━━━━━━━━━━━━━━━━━━

👇 নিচের Category সিলেক্ট করুন
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
            video=NATOK_VIDEO_1,
            caption="""
🎭 Bangla Natok Collection

━━━━━━━━━━━━━━━━━━

✅ Romantic Natok
✅ Funny Natok
✅ Emotional Natok

━━━━━━━━━━━━━━━━━━

🔥 Enjoy Your Video
"""
        )


    # ==========================================
    # Movie
    # ==========================================

    elif query.data == "movie":

        await query.message.reply_video(
            video=MOVIE_VIDEO_1,
            caption="""
🎬 Movie Collection

━━━━━━━━━━━━━━━━━━

✅ Bangla Movie
✅ Hindi Movie
✅ English Movie

━━━━━━━━━━━━━━━━━━

🍿 Enjoy Your Movie
"""
        )


    # ==========================================
    # Collection
    # ==========================================

    elif query.data == "collection":

        await query.message.reply_video(
            video=COLLECTION_VIDEO_1,
            caption="""
😁 Collection Videos

━━━━━━━━━━━━━━━━━━

✅ Viral Videos
✅ Trending Clips
✅ Social Videos

━━━━━━━━━━━━━━━━━━

🔥 Enjoy Your Collection
"""
        )


    # ==========================================
    # Web Series
    # ==========================================

    elif query.data == "series":

        await query.message.reply_video(
            video=SERIES_VIDEO_1,
            caption="""
📺 Web Series Collection

━━━━━━━━━━━━━━━━━━

✅ Bangla Series
✅ Hindi Series
✅ English Series

━━━━━━━━━━━━━━━━━━

🔥 Enjoy Your Series
"""
        )


    # ==========================================
    # Trending
    # ==========================================

    elif query.data == "trending":

        await query.message.reply_video(
            video=TRENDING_VIDEO_1,
            caption="""
🔥 Trending Videos

━━━━━━━━━━━━━━━━━━

✅ Viral Content
✅ Trending Reels
✅ Popular Videos

━━━━━━━━━━━━━━━━━━

🚀 Trending Now
"""
        )


    # ==========================================
    # Funny Clips
    # ==========================================

    elif query.data == "funny":

        await query.message.reply_video(
            video=FUNNY_VIDEO_1,
            caption="""
😂 Funny Clips

━━━━━━━━━━━━━━━━━━

🤣 Meme Videos
🤣 Funny Clips
🤣 Comedy Shorts

━━━━━━━━━━━━━━━━━━

😆 Enjoy Fun Time
"""
        )


# =====================================================
#               FILE ID GETTER SYSTEM
# =====================================================

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # Video File ID
    if update.message.video:

        file_id = update.message.video.file_id

        await update.message.reply_text(
            f"""
🎬 YOUR VIDEO FILE ID 👇

━━━━━━━━━━━━━━━━━━

{file_id}

━━━━━━━━━━━━━━━━━━

✅ Copy This File ID
"""
        )


    # Document File ID
    elif update.message.document:

        file_id = update.message.document.file_id

        await update.message.reply_text(
            f"""
📁 YOUR FILE ID 👇

━━━━━━━━━━━━━━━━━━

{file_id}

━━━━━━━━━━━━━━━━━━

✅ Copy This File ID
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

print("✅ Professional Video Collection Bot Running...")

app.run_polling()
