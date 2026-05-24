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

TOKEN = "8971545585:AAGAVBOLz_epIWnWwj1IQT_viSBp2thdumk"

# =====================================================
#                 MEDIA DATABASE
# =====================================================

# 🎭 Natok Videos
NATOK_VIDEOS = [

    {
        "file_id": "PUT_NATOK_FILE_ID_1",
        "title": "🌸 Romantic Natok"
    },

    {
        "file_id": "PUT_NATOK_FILE_ID_2",
        "title": "😂 Funny Natok"
    }

]

# 🎬 Movie Videos
MOVIE_VIDEOS = [

    {
        "file_id": "PUT_MOVIE_FILE_ID_1",
        "title": "🔥 Bangla Action Movie"
    },

    {
        "file_id": "PUT_MOVIE_FILE_ID_2",
        "title": "❤️ Romantic Movie"
    }

]

# 😁 Collection Videos
COLLECTION_VIDEOS = [

    {
        "file_id": "PUT_COLLECTION_FILE_ID_1",
        "title": "🤣 Funny Viral Video"
    },

    {
        "file_id": "PUT_COLLECTION_FILE_ID_2",
        "title": "🔥 Trending Collection"
    }

]

# 🖼 Photo Collection
PHOTO_FILES = [

    {
        "file_id": "PUT_PHOTO_FILE_ID_1",
        "title": "🌄 Beautiful Wallpaper"
    },

    {
        "file_id": "PUT_PHOTO_FILE_ID_2",
        "title": "🔥 HD Photo"
    }

]

# 🎮 Game Files
GAME_FILES = [

    {
        "file_id": "PUT_GAME_FILE_ID_1",
        "title": "🎮 GTA Game"
    },

    {
        "file_id": "PUT_GAME_FILE_ID_2",
        "title": "🔥 Android Game"
    }

]

# 💻 Software Files
SOFTWARE_FILES = [

    {
        "file_id": "PUT_SOFTWARE_FILE_ID_1",
        "title": "💻 Premium Software"
    },

    {
        "file_id": "PUT_SOFTWARE_FILE_ID_2",
        "title": "🔥 Windows Tool"
    }

]

# =====================================================
#                     START MENU
# =====================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [

        [InlineKeyboardButton("🎭 Natok", callback_data="natok_0")],

        [InlineKeyboardButton("🎬 Movie", callback_data="movie_0")],

        [InlineKeyboardButton("😁 Collection", callback_data="collection_0")],

        [InlineKeyboardButton("🖼 Photo", callback_data="photo_0")],

        [InlineKeyboardButton("🎮 Game", callback_data="game_0")],

        [InlineKeyboardButton("💻 Software", callback_data="software_0")]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    text = """
🎬 Welcome To Video Collection 🎬

━━━━━━━━━━━━━━━━━━

🔥 Premium Media Collection Bot

✅ Natok
✅ Movie
✅ Collection
✅ Photos
✅ Games
✅ Software

━━━━━━━━━━━━━━━━━━

👇 নিচের Category সিলেক্ট করুন
"""

    await update.message.reply_text(
        text,
        reply_markup=reply_markup
    )

# =====================================================
#                   BUTTON SYSTEM
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

            [InlineKeyboardButton("🖼 Photo", callback_data="photo_0")],

            [InlineKeyboardButton("🎮 Game", callback_data="game_0")],

            [InlineKeyboardButton("💻 Software", callback_data="software_0")]

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

        if index > 0:

            keyboard.append(
                InlineKeyboardButton(
                    "⏮ Previous",
                    callback_data=f"natok_{index-1}"
                )
            )

        if index < len(NATOK_VIDEOS) - 1:

            keyboard.append(
                InlineKeyboardButton(
                    "⏭ Next",
                    callback_data=f"natok_{index+1}"
                )
            )

        nav_buttons = [keyboard]

        nav_buttons.append(
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        )

        reply_markup = InlineKeyboardMarkup(nav_buttons)

        await query.message.reply_video(
            video=NATOK_VIDEOS[index]["file_id"],
            caption=NATOK_VIDEOS[index]["title"],
            reply_markup=reply_markup
        )

# =====================================================
# MOVIE SYSTEM
# =====================================================

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
            video=MOVIE_VIDEOS[index]["file_id"],
            caption=MOVIE_VIDEOS[index]["title"],
            reply_markup=reply_markup
        )

# =====================================================
# COLLECTION SYSTEM
# =====================================================

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
            video=COLLECTION_VIDEOS[index]["file_id"],
            caption=COLLECTION_VIDEOS[index]["title"],
            reply_markup=reply_markup
        )

# =====================================================
# PHOTO SYSTEM
# =====================================================

    elif data.startswith("photo_"):

        index = int(data.split("_")[1])

        keyboard = []

        if index > 0:

            keyboard.append(
                InlineKeyboardButton(
                    "⏮ Previous",
                    callback_data=f"photo_{index-1}"
                )
            )

        if index < len(PHOTO_FILES) - 1:

            keyboard.append(
                InlineKeyboardButton(
                    "⏭ Next",
                    callback_data=f"photo_{index+1}"
                )
            )

        nav_buttons = [keyboard]

        nav_buttons.append(
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        )

        reply_markup = InlineKeyboardMarkup(nav_buttons)

        await query.message.reply_photo(
            photo=PHOTO_FILES[index]["file_id"],
            caption=PHOTO_FILES[index]["title"],
            reply_markup=reply_markup
        )

# =====================================================
# GAME SYSTEM
# =====================================================

    elif data.startswith("game_"):

        index = int(data.split("_")[1])

        keyboard = []

        if index > 0:

            keyboard.append(
                InlineKeyboardButton(
                    "⏮ Previous",
                    callback_data=f"game_{index-1}"
                )
            )

        if index < len(GAME_FILES) - 1:

            keyboard.append(
                InlineKeyboardButton(
                    "⏭ Next",
                    callback_data=f"game_{index+1}"
                )
            )

        nav_buttons = [keyboard]

        nav_buttons.append(
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        )

        reply_markup = InlineKeyboardMarkup(nav_buttons)

        await query.message.reply_document(
            document=GAME_FILES[index]["file_id"],
            caption=GAME_FILES[index]["title"],
            reply_markup=reply_markup
        )

# =====================================================
# SOFTWARE SYSTEM
# =====================================================

    elif data.startswith("software_"):

        index = int(data.split("_")[1])

        keyboard = []

        if index > 0:

            keyboard.append(
                InlineKeyboardButton(
                    "⏮ Previous",
                    callback_data=f"software_{index-1}"
                )
            )

        if index < len(SOFTWARE_FILES) - 1:

            keyboard.append(
                InlineKeyboardButton(
                    "⏭ Next",
                    callback_data=f"software_{index+1}"
                )
            )

        nav_buttons = [keyboard]

        nav_buttons.append(
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        )

        reply_markup = InlineKeyboardMarkup(nav_buttons)

        await query.message.reply_document(
            document=SOFTWARE_FILES[index]["file_id"],
            caption=SOFTWARE_FILES[index]["title"],
            reply_markup=reply_markup
        )

# =====================================================
# FILE ID GETTER
# =====================================================

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.video:

        file_id = update.message.video.file_id

        await update.message.reply_text(
            f"🎬 VIDEO FILE ID 👇\n\n{file_id}"
        )

    elif update.message.photo:

        file_id = update.message.photo[-1].file_id

        await update.message.reply_text(
            f"🖼 PHOTO FILE ID 👇\n\n{file_id}"
        )

    elif update.message.document:

        file_id = update.message.document.file_id

        await update.message.reply_text(
            f"📁 DOCUMENT FILE ID 👇\n\n{file_id}"
        )

# =====================================================
# MAIN SYSTEM
# =====================================================

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(CallbackQueryHandler(button))

app.add_handler(
    MessageHandler(
        filters.VIDEO |
        filters.PHOTO |
        filters.Document.ALL,
        get_file_id
    )
)

print("✅ Professional Media Collection Bot Running...")

app.run_polling()
