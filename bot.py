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
#               TELEGRAM FILE DATABASE
# =====================================================

# 🎭 Natok Videos
NATOK_VIDEOS = [
    "PUT_NATOK_FILE_ID_1",
    "PUT_NATOK_FILE_ID_2"
]

# 🎬 Movie Videos
MOVIE_VIDEOS = [
    "PUT_MOVIE_FILE_ID_1",
    "PUT_MOVIE_FILE_ID_2"
]

# 😁 Collection Videos
COLLECTION_VIDEOS = [
    "PUT_COLLECTION_FILE_ID_1",
    "PUT_COLLECTION_FILE_ID_2"
]

# 🖼 Photo Collection
PHOTO_FILES = [
    "PUT_PHOTO_FILE_ID_1",
    "PUT_PHOTO_FILE_ID_2"
]

# 🎮 Game Files
GAME_FILES = [
    "PUT_GAME_FILE_ID_1",
    "PUT_GAME_FILE_ID_2"
]

# 💻 Software Files
SOFTWARE_FILES = [
    "PUT_SOFTWARE_FILE_ID_1",
    "PUT_SOFTWARE_FILE_ID_2"
]


# =====================================================
#                  START COMMAND
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
    # NATOK VIDEOS
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
            video=NATOK_VIDEOS[index],
            caption=f"🎭 Natok Video {index+1}",
            reply_markup=reply_markup
        )


    # =================================================
    # MOVIE VIDEOS
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
            caption=f"🎬 Movie Video {index+1}",
            reply_markup=reply_markup
        )


    # =================================================
    # COLLECTION VIDEOS
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
            caption=f"😁 Collection Video {index+1}",
            reply_markup=reply_markup
        )


    # =================================================
    # PHOTO SYSTEM
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
            photo=PHOTO_FILES[index],
            caption=f"🖼 Photo {index+1}",
            reply_markup=reply_markup
        )


    # =================================================
    # GAME FILE SYSTEM
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
            document=GAME_FILES[index],
            caption=f"🎮 Game File {index+1}",
            reply_markup=reply_markup
        )


    # =================================================
    # SOFTWARE FILE SYSTEM
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
            document=SOFTWARE_FILES[index],
            caption=f"💻 Software File {index+1}",
            reply_markup=reply_markup
        )


# =====================================================
#               FILE ID GETTER SYSTEM
# =====================================================

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # VIDEO FILE ID
    if update.message.video:

        file_id = update.message.video.file_id

        await update.message.reply_text(
            f"🎬 VIDEO FILE ID 👇\n\n{file_id}"
        )

    # PHOTO FILE ID
    elif update.message.photo:

        file_id = update.message.photo[-1].file_id

        await update.message.reply_text(
            f"🖼 PHOTO FILE ID 👇\n\n{file_id}"
        )

    # DOCUMENT FILE ID
    elif update.message.document:

        file_id = update.message.document.file_id

        await update.message.reply_text(
            f"📁 DOCUMENT FILE ID 👇\n\n{file_id}"
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
        filters.VIDEO |
        filters.PHOTO |
        filters.Document.ALL,
        get_file_id
    )
)

print("✅ Professional Media Collection Bot Running...")

app.run_polling()