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
#                 MEDIA DATABASE
# =====================================================

# 🎭 NATOK VIDEOS
NATOK_VIDEOS = [

    {"file_id": "BAACAgQAAxkBAAPgahK2TYQulqzTJukOW1w0PZipp0gAAkocAALPgYBQSWN5XsFZunU7BA", "title": "Bachelor.Point.S05E89."},
    {"file_id": "BAACAgQAAxkBAAIBAAFqErtNrxO_Xa2nhb7FRfEBYOsaaQACTBwAAs-BgFADGsLbamWtkzsE", "title": "Bachelor.Point.S05E90"},
    {"file_id": "BAACAgQAAxkBAAIBEWoSw7nuZ95iaTSWQgLSnLULMteTAAJOHAACz4GAUBfOuMfOLPLnOwQ", "title": "Bachelor.Point.S05E91"},
    {"file_id": "PUT_NATOK_FILE_ID_4", "title": "Natok 4"},
    {"file_id": "PUT_NATOK_FILE_ID_5", "title": "Natok 5"}

]

# 🎬 MOVIE VIDEOS
MOVIE_VIDEOS = [

    {"file_id": "PUT_MOVIE_FILE_ID_1", "title": "Movie 1"},
    {"file_id": "PUT_MOVIE_FILE_ID_2", "title": "Movie 2"},
    {"file_id": "PUT_MOVIE_FILE_ID_3", "title": "Movie 3"},
    {"file_id": "PUT_MOVIE_FILE_ID_4", "title": "Movie 4"},
    {"file_id": "PUT_MOVIE_FILE_ID_5", "title": "Movie 5"}

]

# 😁 COLLECTION VIDEOS
COLLECTION_VIDEOS = [

    {"file_id": "PUT_COLLECTION_FILE_ID_1", "title": "Collection 1"},
    {"file_id": "PUT_COLLECTION_FILE_ID_2", "title": "Collection 2"},
    {"file_id": "PUT_COLLECTION_FILE_ID_3", "title": "Collection 3"},
    {"file_id": "PUT_COLLECTION_FILE_ID_4", "title": "Collection 4"},
    {"file_id": "PUT_COLLECTION_FILE_ID_5", "title": "Collection 5"}

]

# 🖼 PHOTO FILES
PHOTO_FILES = [

    {"file_id": "PUT_PHOTO_FILE_ID_1", "title": "Photo 1"},
    {"file_id": "PUT_PHOTO_FILE_ID_2", "title": "Photo 2"},
    {"file_id": "PUT_PHOTO_FILE_ID_3", "title": "Photo 3"},
    {"file_id": "PUT_PHOTO_FILE_ID_4", "title": "Photo 4"},
    {"file_id": "PUT_PHOTO_FILE_ID_5", "title": "Photo 5"}

]

# 🎮 GAME FILES
GAME_FILES = [

    {"file_id": "PUT_GAME_FILE_ID_1", "title": "Game 1"},
    {"file_id": "PUT_GAME_FILE_ID_2", "title": "Game 2"},
    {"file_id": "PUT_GAME_FILE_ID_3", "title": "Game 3"},
    {"file_id": "PUT_GAME_FILE_ID_4", "title": "Game 4"},
    {"file_id": "PUT_GAME_FILE_ID_5", "title": "Game 5"}

]

# 💻 SOFTWARE FILES
SOFTWARE_FILES = [

    {"file_id": "PUT_SOFTWARE_FILE_ID_1", "title": "Software 1"},
    {"file_id": "PUT_SOFTWARE_FILE_ID_2", "title": "Software 2"},
    {"file_id": "PUT_SOFTWARE_FILE_ID_3", "title": "Software 3"},
    {"file_id": "PUT_SOFTWARE_FILE_ID_4", "title": "Software 4"},
    {"file_id": "PUT_SOFTWARE_FILE_ID_5", "title": "Software 5"}

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
    # NATOK
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


    # =================================================
    # MOVIE
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
            video=MOVIE_VIDEOS[index]["file_id"],
            caption=MOVIE_VIDEOS[index]["title"],
            reply_markup=reply_markup
        )


    # =================================================
    # COLLECTION
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
            video=COLLECTION_VIDEOS[index]["file_id"],
            caption=COLLECTION_VIDEOS[index]["title"],
            reply_markup=reply_markup
        )


    # =================================================
    # PHOTO
    # =================================================

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


    # =================================================
    # GAME
    # =================================================

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


    # =================================================
    # SOFTWARE
    # =================================================

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
#               FILE ID GETTER SYSTEM
# =====================================================

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # VIDEO
    if update.message.video:

        file_id = update.message.video.file_id

        await update.message.reply_text(
            f"🎬 VIDEO FILE ID 👇\n\n{file_id}"
        )

    # PHOTO
    elif update.message.photo:

        file_id = update.message.photo[-1].file_id

        await update.message.reply_text(
            f"🖼 PHOTO FILE ID 👇\n\n{file_id}"
        )

    # DOCUMENT
    elif update.message.document:

        file_id = update.message.document.file_id

        await update.message.reply_text(
            f"📁 DOCUMENT FILE ID 👇\n\n{file_id}"
        )


# =====================================================
#                     MAIN SYSTEM
# =====================================================

app = Application.builder().token(TOKEN).build()

# START COMMAND
app.add_handler(CommandHandler("start", start))

# BUTTON SYSTEM
app.add_handler(CallbackQueryHandler(button))

# FILE ID GETTER
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