from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update
)

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
#                ADMIN USER ID
# =====================================================

ADMIN_ID = 7727343195


# =====================================================
#               TELEGRAM VIDEO FILE IDs
# =====================================================

NATOK_VIDEOS = [
    "PUT_NATOK_FILE_ID_1",
    "PUT_NATOK_FILE_ID_2"
]

MOVIE_VIDEOS = [
    "PUT_MOVIE_FILE_ID_1",
    "PUT_MOVIE_FILE_ID_2"
]

COLLECTION_VIDEOS = [
    "PUT_COLLECTION_FILE_ID_1",
    "PUT_COLLECTION_FILE_ID_2"
]


# =====================================================
#                  START COMMAND
# =====================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [

        [InlineKeyboardButton("🎭 Natok", callback_data="natok_0")],

        [InlineKeyboardButton("🎬 Movie", callback_data="movie_0")],

        [InlineKeyboardButton("😁 Collection", callback_data="collection_0")],

        [InlineKeyboardButton("🔎 Search", callback_data="search")],

        [InlineKeyboardButton("👨‍💻 Admin Panel", callback_data="admin")]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    text = """
🎬 Welcome To Video Collection 🎬

━━━━━━━━━━━━━━━━━━

🔥 Professional Video Bot

✅ Natok
✅ Movie
✅ Collection
✅ Search System
✅ Next / Previous
✅ Back Button

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

    data = query.data


    # =================================================
    # BACK BUTTON
    # =================================================

    if data == "back":

        keyboard = [

            [InlineKeyboardButton("🎭 Natok", callback_data="natok_0")],

            [InlineKeyboardButton("🎬 Movie", callback_data="movie_0")],

            [InlineKeyboardButton("😁 Collection", callback_data="collection_0")],

            [InlineKeyboardButton("🔎 Search", callback_data="search")]

        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.message.reply_text(
            "🔙 Main Menu",
            reply_markup=reply_markup
        )


    # =================================================
    # NATOK SYSTEM
    # =================================================

    elif data.startswith("natok_"):

        index = int(data.split("_")[1])

        keyboard = []

        # Previous Button
        if index > 0:

            keyboard.append(
                InlineKeyboardButton(
                    "⏮ Previous",
                    callback_data=f"natok_{index-1}"
                )
            )

        # Next Button
        if index < len(NATOK_VIDEOS) - 1:

            keyboard.append(
                InlineKeyboardButton(
                    "⏭ Next",
                    callback_data=f"natok_{index+1}"
                )
            )

        nav_buttons = [keyboard]

        # Back Button
        nav_buttons.append(
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        )

        reply_markup = InlineKeyboardMarkup(nav_buttons)

        await query.message.reply_video(
            video=NATOK_VIDEOS[index],
            caption=f"""
🎭 Natok Collection

📁 Video Number: {index+1}

🔥 Enjoy Your Video
""",
            reply_markup=reply_markup
        )


    # =================================================
    # MOVIE SYSTEM
    # =================================================

    elif data.startswith("movie_"):

        index = int(data.split("_")[1])

        keyboard = []

        if index > 0:

            keyboard.append(
                InlineKeyboardButton(
                    "⏮ Previous",
                    callback_data=f"movie_{index-1}"
                )
            )

        if index < len(MOVIE_VIDEOS) - 1:

            keyboard.append(
                InlineKeyboardButton(
                    "⏭ Next",
                    callback_data=f"movie_{index+1}"
                )
            )

        nav_buttons = [keyboard]

        nav_buttons.append(
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        )

        reply_markup = InlineKeyboardMarkup(nav_buttons)

        await query.message.reply_video(
            video=MOVIE_VIDEOS[index],
            caption=f"""
🎬 Movie Collection

📁 Video Number: {index+1}

🍿 Enjoy Your Movie
""",
            reply_markup=reply_markup
        )


    # =================================================
    # COLLECTION SYSTEM
    # =================================================

    elif data.startswith("collection_"):

        index = int(data.split("_")[1])

        keyboard = []

        if index > 0:

            keyboard.append(
                InlineKeyboardButton(
                    "⏮ Previous",
                    callback_data=f"collection_{index-1}"
                )
            )

        if index < len(COLLECTION_VIDEOS) - 1:

            keyboard.append(
                InlineKeyboardButton(
                    "⏭ Next",
                    callback_data=f"collection_{index+1}"
                )
            )

        nav_buttons = [keyboard]

        nav_buttons.append(
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        )

        reply_markup = InlineKeyboardMarkup(nav_buttons)

        await query.message.reply_video(
            video=COLLECTION_VIDEOS[index],
            caption=f"""
😁 Collection Videos

📁 Video Number: {index+1}

🔥 Enjoy Your Collection
""",
            reply_markup=reply_markup
        )


    # =================================================
    # SEARCH SYSTEM
    # =================================================

    elif data == "search":

        await query.message.reply_text(
            """
🔎 Search System

Movie/Natok Name লিখুন।
"""
        )


    # =================================================
    # ADMIN PANEL
    # =================================================

    elif data == "admin":

        if query.from_user.id != ADMIN_ID:

            await query.message.reply_text(
                "❌ Only Admin Can Access"
            )

            return

        await query.message.reply_text(
            """
👨‍💻 Admin Panel

✅ Upload Videos
✅ Delete Videos
✅ Broadcast Message
✅ User Statistics
"""
        )


# =====================================================
#                  SEARCH SYSTEM
# =====================================================

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text.lower()

    if "movie" in text:

        await update.message.reply_text(
            "🎬 Movie Found"
        )

    elif "natok" in text:

        await update.message.reply_text(
            "🎭 Natok Found"
        )

    else:

        await update.message.reply_text(
            "❌ No Result Found"
        )


# =====================================================
#                FILE ID GETTER SYSTEM
# =====================================================

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):

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
        filters.VIDEO,
        get_file_id
    )
)

# Search System
app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        search
    )
)

print("✅ Professional Video Collection Bot Running...")

app.run_polling()
