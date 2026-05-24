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

from fuzzywuzzy import fuzz

# =====================================================
#                     BOT TOKEN
# =====================================================

TOKEN = "8971545585:AAGAVBOLz_epIWnWwj1IQT_viSBp2thdumk"

# =====================================================
#                 MEDIA DATABASE
# =====================================================

DATABASE = {

    "natok": [

        {
            "file_id": "PUT_NATOK_FILE_ID",
            "title": "Bachelor Point Episode 1",
            "type": "video"
        }

    ],

    "movie": [

        {
            "file_id": "PUT_MOVIE_FILE_ID",
            "title": "Movie 1",
            "type": "video"
        }

    ],

    "collection": [

        {
            "file_id": "PUT_COLLECTION_FILE_ID",
            "title": "Private Video",
            "type": "video"
        }

    ],

    "photo": [

        {
            "file_id": "PUT_PHOTO_FILE_ID",
            "title": "Photo 1",
            "type": "photo"
        }

    ],

    "game": [

        {
            "file_id": "PUT_GAME_FILE_ID",
            "title": "Game 1",
            "type": "document"
        }

    ],

    "software": [

        {
            "file_id": "PUT_SOFTWARE_FILE_ID",
            "title": "Software 1",
            "type": "document"
        }

    ]

}

# =====================================================
#               COLLECTION PASSWORD
# =====================================================

COLLECTION_PASSWORD = "20200"

# =====================================================
#                  MAIN MENU
# =====================================================

def main_menu():

    keyboard = [

        [InlineKeyboardButton("🎭 Natok", callback_data="natok_0")],

        [InlineKeyboardButton("🎬 Movie", callback_data="movie_0")],

        [InlineKeyboardButton("🔞 Collection", callback_data="collection_lock")],

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
🎬 Welcome To Media Bot 🎬

━━━━━━━━━━━━━━━━━━

🔥 Premium Entertainment Hub

🎭 Natok
🎬 Movie
🖼 Photo
🎮 Game
💻 Software

━━━━━━━━━━━━━━━━━━

🔍 Smart Search Enabled
⚡ Fast Media System
🚀 Unlimited Media Support

━━━━━━━━━━━━━━━━━━

👇 Select Category
"""

    await update.message.reply_text(

        text,

        reply_markup=main_menu()

    )

# =====================================================
#                    BUTTON SYSTEM
# =====================================================

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    data = query.data

    # BACK
    if data == "back":

        await query.message.reply_text(

            "🔙 Main Menu",

            reply_markup=main_menu()

        )

        return

    # PASSWORD
    if data == "collection_lock":

        context.user_data["waiting_password"] = True

        await query.message.reply_text(

            "🔒 Enter Collection Password"

        )

        return

    category = data.split("_")[0]

    index = int(data.split("_")[1])

    media_list = DATABASE.get(category, [])

    if len(media_list) == 0:

        await query.message.reply_text(

            "❌ No Media Found"

        )

        return

    media = media_list[index]

    buttons = []

    row = []

    if index > 0:

        row.append(

            InlineKeyboardButton(

                "⏮ Previous",

                callback_data=f"{category}_{index-1}"

            )

        )

    if index < len(media_list) - 1:

        row.append(

            InlineKeyboardButton(

                "⏭ Next",

                callback_data=f"{category}_{index+1}"

            )

        )

    if row:

        buttons.append(row)

    buttons.append(

        [InlineKeyboardButton("🔙 Back", callback_data="back")]

    )

    reply_markup = InlineKeyboardMarkup(buttons)

    file_id = media["file_id"]

    title = media["title"]

    media_type = media["type"]

    # VIDEO
    if media_type == "video":

        await query.message.reply_video(

            video=file_id,

            caption=f"🎬 {title}",

            reply_markup=reply_markup

        )

    # PHOTO
    elif media_type == "photo":

        await query.message.reply_photo(

            photo=file_id,

            caption=f"🖼 {title}",

            reply_markup=reply_markup

        )

    # DOCUMENT
    else:

        await query.message.reply_document(

            document=file_id,

            caption=f"📁 {title}",

            reply_markup=reply_markup

        )

# =====================================================
#                  SEARCH SYSTEM
# =====================================================

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text.lower()

    # PASSWORD
    if context.user_data.get("waiting_password"):

        if text == COLLECTION_PASSWORD:

            context.user_data["waiting_password"] = False

            keyboard = [

                [

                    InlineKeyboardButton(

                        "🔥 Open Collection",

                        callback_data="collection_0"

                    )

                ]

            ]

            await update.message.reply_text(

                "✅ Collection Unlocked",

                reply_markup=InlineKeyboardMarkup(keyboard)

            )

        else:

            await update.message.reply_text(

                "❌ Wrong Password"

            )

        return

    results = []

    for category in DATABASE:

        for media in DATABASE[category]:

            score = fuzz.partial_ratio(

                text,

                media["title"].lower()

            )

            if score > 70:

                results.append(media)

    if len(results) == 0:

        await update.message.reply_text(

            "❌ No Result Found"

        )

        return

    for media in results:

        file_id = media["file_id"]

        title = media["title"]

        media_type = media["type"]

        if media_type == "video":

            await update.message.reply_video(

                video=file_id,

                caption=f"🎬 {title}"

            )

        elif media_type == "photo":

            await update.message.reply_photo(

                photo=file_id,

                caption=f"🖼 {title}"

            )

        else:

            await update.message.reply_document(

                document=file_id,

                caption=f"📁 {title}"

            )

# =====================================================
#                FILE ID GETTER
# =====================================================

async def fileid(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.video:

        await update.message.reply_text(

            update.message.video.file_id

        )

    elif update.message.photo:

        await update.message.reply_text(

            update.message.photo[-1].file_id

        )

    elif update.message.document:

        await update.message.reply_text(

            update.message.document.file_id

        )

# =====================================================
#                     MAIN APP
# =====================================================

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(CallbackQueryHandler(button))

app.add_handler(

    MessageHandler(

        filters.TEXT & ~filters.COMMAND,

        search

    )

)

app.add_handler(

    MessageHandler(

        filters.VIDEO |

        filters.PHOTO |

        filters.Document.ALL,

        fileid

    )

)

print("✅ Media Bot Running...")

app.run_polling(drop_pending_updates=True)
