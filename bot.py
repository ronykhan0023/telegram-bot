from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# =====================================================
#                    BOT TOKEN
# =====================================================

TOKEN = "8971545585:AAGAVBOLz_epIWnWwj1IQT_viSBp2thdumk"

# =====================================================
#                  MEDIA DATABASE
# =====================================================

NATOK = [

    {
        "file_id": "PUT_NATOK_FILE_ID_1",
        "title": "Bachelor Point Episode 1"
    },

    {
        "file_id": "PUT_NATOK_FILE_ID_2",
        "title": "Funny Natok Episode"
    }

]

MOVIE = [

    {
        "file_id": "PUT_MOVIE_FILE_ID_1",
        "title": "Bangla Action Movie"
    },

    {
        "file_id": "PUT_MOVIE_FILE_ID_2",
        "title": "Romantic Movie"
    }

]

COLLECTION = [

    {
        "file_id": "PUT_COLLECTION_FILE_ID_1",
        "title": "Funny Viral Video"
    },

    {
        "file_id": "PUT_COLLECTION_FILE_ID_2",
        "title": "Trending Collection"
    }

]

PHOTO = [

    {
        "file_id": "PUT_PHOTO_FILE_ID_1",
        "title": "Beautiful Photo"
    },

    {
        "file_id": "PUT_PHOTO_FILE_ID_2",
        "title": "HD Wallpaper"
    }

]

GAME = [

    {
        "file_id": "PUT_GAME_FILE_ID_1",
        "title": "Android Game"
    },

    {
        "file_id": "PUT_GAME_FILE_ID_2",
        "title": "PC Game"
    }

]

SOFTWARE = [

    {
        "file_id": "PUT_SOFTWARE_FILE_ID_1",
        "title": "Premium Software"
    },

    {
        "file_id": "PUT_SOFTWARE_FILE_ID_2",
        "title": "Windows Tool"
    }

]

# =====================================================
#                    MAIN MENU
# =====================================================

def menu():

    keyboard = [

        [InlineKeyboardButton("🎭 Natok", callback_data="natok_0")],

        [InlineKeyboardButton("🎬 Movie", callback_data="movie_0")],

        [InlineKeyboardButton("😁 Collection", callback_data="collection_0")],

        [InlineKeyboardButton("🖼 Photo", callback_data="photo_0")],

        [InlineKeyboardButton("🎮 Game", callback_data="game_0")],

        [InlineKeyboardButton("💻 Software", callback_data="software_0")]

    ]

    return InlineKeyboardMarkup(keyboard)

# =====================================================
#                      START
# =====================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🎬 Welcome To Premium Media Bot 🎬

━━━━━━━━━━━━━━━━━━

🔥 Entertainment Collection

✅ Natok
✅ Movie
✅ Collection
✅ Photo
✅ Game
✅ Software

━━━━━━━━━━━━━━━━━━

📥 Send Any File To Get File ID

👇 Select Category
"""

    await update.message.reply_text(

        text,

        reply_markup=menu()

    )

# =====================================================
#                   BUTTON SYSTEM
# =====================================================

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    data = query.data

    # =================================================
    # BACK BUTTON
    # =================================================

    if data == "back":

        await query.message.reply_text(

            "🔙 Main Menu",

            reply_markup=menu()

        )

        return

    # =================================================
    # CATEGORY SELECT
    # =================================================

    category = data.split("_")[0]

    index = int(data.split("_")[1])

    if category == "natok":

        media_list = NATOK
        media_type = "video"

    elif category == "movie":

        media_list = MOVIE
        media_type = "video"

    elif category == "collection":

        media_list = COLLECTION
        media_type = "video"

    elif category == "photo":

        media_list = PHOTO
        media_type = "photo"

    elif category == "game":

        media_list = GAME
        media_type = "document"

    elif category == "software":

        media_list = SOFTWARE
        media_type = "document"

    else:

        return

    media = media_list[index]

    file_id = media["file_id"]

    title = media["title"]

    # =================================================
    # NEXT PREVIOUS BUTTON
    # =================================================

    nav = []

    if index > 0:

        nav.append(

            InlineKeyboardButton(

                "⏮ Previous",

                callback_data=f"{category}_{index-1}"

            )

        )

    if index < len(media_list) - 1:

        nav.append(

            InlineKeyboardButton(

                "⏭ Next",

                callback_data=f"{category}_{index+1}"

            )

        )

    keyboard = []

    if nav:

        keyboard.append(nav)

    keyboard.append(

        [InlineKeyboardButton("🔙 Back", callback_data="back")]

    )

    reply_markup = InlineKeyboardMarkup(keyboard)

    # =================================================
    # SEND MEDIA
    # =================================================

    if media_type == "video":

        await query.message.reply_video(

            video=file_id,

            caption=f"🎬 {title}",

            reply_markup=reply_markup

        )

    elif media_type == "photo":

        await query.message.reply_photo(

            photo=file_id,

            caption=f"🖼 {title}",

            reply_markup=reply_markup

        )

    else:

        await query.message.reply_document(

            document=file_id,

            caption=f"📁 {title}",

            reply_markup=reply_markup

        )

# =====================================================
#                  FILE ID GETTER
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
#                    MAIN APP
# =====================================================

app = Application.builder().token(TOKEN).build()

# START COMMAND
app.add_handler(CommandHandler("start", start))

# BUTTON HANDLER
app.add_handler(CallbackQueryHandler(buttons))

# FILE ID GETTER
app.add_handler(

    MessageHandler(

        filters.VIDEO |
        filters.PHOTO |
        filters.Document.ALL,

        get_file_id

    )

)

print("✅ Premium Media Bot Running...")

# =====================================================
#                    RUN BOT
# =====================================================

app.run_polling()
