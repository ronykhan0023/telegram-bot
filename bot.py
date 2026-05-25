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
    ContextTypes,
    filters
)

from difflib import get_close_matches

# =====================================================
#                    BOT TOKEN
# =====================================================

TOKEN = "8971545585:AAGAVBOLz_epIWnWwj1IQT_viSBp2thdumk"

# =====================================================
#                 COLLECTION PASSWORD
# =====================================================

COLLECTION_PASSWORD = "20200"

# =====================================================
#                  MEDIA DATABASE
# =====================================================

DATABASE = {

    "natok": [

        {
            "file_id": "BAACAgQAAxkBAAICimoTGVa54DPeYC7eCJrjCeUZajODAALHHAACr4QJUuQ74TwPCnlrOwQ",
            "title": "Love Sitter 2026 Natok",
            "type": "video"
        },

        {
            "file_id": "BAACAgQAAxkBAAICj2oTom-VgVThmsKGanTulRacZOZIAAKsIQACTYGAUHSiOvSDlXkwOwQ",
            "title": "Bachalor Point 89-96 ",
            "type": "video"
        }

    ],

    "movie": [

        {
            "file_id": "BAACAgQAAxkBAAICI2oTDgt7xzYq-JsK5ug8-fZkk9FwAAIFHwACEXp5UE4b9rHtyTAeOwQ",
            "title": "Prince Movie 2026",
            "type": "video"
        },

        {
            "file_id": "BAACAgQAAxkBAAICJWoTDiARNUay6SvChYHP0hdrUhcOAAJoGgACUOkZUYY9J1psrdFWOwQ",
            "title": "Supar Man 2025 Bangla",
            "type": "video"
        },
 {
            "file_id": "BAACAgEAAxkBAAICJ2oTDjgZze1yUuWdwbiSVZ0wqcw9AALBBgAC8kbpR6d71xSqa9BkOwQ",
            "title": "Nat Boltu Vuter Bari",
            "type": "video"
        },
{
            "file_id": "BAACAgEAAxkBAAICO2oTExBkWwIk2Yd-6tROlC2K8nc7AALoFQACDZewRugIYHs5k2LyOwQ",
            "title": "Prince Movie 2026",
            "type": "video"
        },
{
            "file_id": "BAACAgQAAxkBAAICPGoTExDFfTMIeHld_86tnnSltBRcAAKPIwAC8csRU6jgm6gIzmA6OwQ",
            "title": "Rakkhosh Movie 2026",
            "type": "video"
        },
{
            "file_id": "BAACAgUAAxkBAAICPWoTExB8YKywmw_y5Gycg7ylqX3HAAJVIAACFzvBVmpXbtskOj1FOwQ",
            "title": "Dhurdhar Revenge",
            "type": "video"
        },
{
            "file_id": "BAACAgUAAxkBAAICPmoTExAjuAk-udCYOtu9CBQ1lxb2AAJEGgACZfkRVtnPjOB_t72bOwQ",
            "title": "Borbad Movie Sakib Khan",
            "type": "video"
        },
{
            "file_id": "BAACAgUAAxkBAAICP2oTExDFNSfmrPyLQc7Q9xDd75iSAAJFGgACZfkRVpredSl1rpIhOwQ",
            "title": "Daagi Movie 2025",
            "type": "video"
        },
{
            "file_id": "BAACAgQAAxkBAAICQGoTExBLPgs9Ec-VTSF5cKl06GDLAAINHgACXKZZU5FH-ZcygQTmOwQ",
            "title": "Paap Kaheni 2",
            "type": "video"
        },
{
            "file_id": "BAACAgQAAxkBAAICQWoTExA8DrbLEk-2yvzcnt3zihK4AAJlHQACj7GoUAxKxdANH-uyOwQ",
            "title": "Ramaro on duty 2022 Bangla dubbed Movie",
            "type": "video"
        },
{
            "file_id": "BAACAgQAAxkBAAICSWoTFPSwLE552zADG0j53gmOb6ztAAKwHQAC8IKhUEdTZ1cwxK7KOwQ",
            "title": "Tandob Sakib Khan",
            "type": "video"
        },
{    "file_id": "BAACAgQAAxkBAAICbmoTFgABumi_CQazYQd3_VG-ROUNfAADJgACcE4oUmRjlzmPoenMOwQ",
"title": "Chokro seson 2",
"type": "video"
},
{  "file_id": "BAACAgEAAxkBAAICb2oTFgABaS_aVTkcJfuVrKO5Lo0hWgACuQUAAnNUkEZ-anaI5pie9jsE",
            "title": "Prince Movie Sakib Khan",
            "type": "video"
        },
    ],

    "collection": [

        {
            "file_id": "BAACAgQAAxkBAAICF2oTDMgYY_kDu4j-mqnnKEt-jRmPAAJjCAACL0MoUcjPTUZg6l9-OwQ",
            "title": "pompom 1",
            "type": "video"
        },

        {
            "file_id": "PUT_COLLECTION_FILE_ID_2",
            "title": "Private Collection 2",
            "type": "video"
        }

    ],

    "photo": [

        {
            "file_id": "PUT_PHOTO_FILE_ID_1",
            "title": "Beautiful Wallpaper",
            "type": "photo"
        }

    ],

    "game": [

        {
            "file_id": "PUT_GAME_FILE_ID_1",
            "title": "Android Game",
            "type": "document"
        }

    ],

    "software": [

        {
            "file_id": "PUT_SOFTWARE_FILE_ID_1",
            "title": "Premium Software",
            "type": "document"
        }

    ]

}

# =====================================================
#                     MAIN MENU
# =====================================================

def main_menu():

    keyboard = [

        [InlineKeyboardButton("🎭 Natok", callback_data="natok_0")],

        [InlineKeyboardButton("🎬 Movie", callback_data="movie_0")],

        [InlineKeyboardButton("🔒 Collection", callback_data="collection_password")],

        [InlineKeyboardButton("🖼 Photo", callback_data="photo_0")],

        [InlineKeyboardButton("🎮 Game", callback_data="game_0")],

        [InlineKeyboardButton("💻 Software", callback_data="software_0")]

    ]

    return InlineKeyboardMarkup(keyboard)

# =====================================================
#                       START
# =====================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🎬 Welcome To Premium Media Bot 🎬

━━━━━━━━━━━━━━━━━━

🔥 Smart Entertainment System

✅ Natok
✅ Movie
✅ Locked Collection
✅ Photo
✅ Game
✅ Software

━━━━━━━━━━━━━━━━━━

🔍 Smart Search Available
📥 Send File To Get File ID

━━━━━━━━━━━━━━━━━━

👇 Select Category
"""

    await update.message.reply_text(

        text,

        reply_markup=main_menu()

    )

# =====================================================
#                  SEND MEDIA
# =====================================================

async def send_media(query, category, index):

    media_list = DATABASE[category]

    media = media_list[index]

    file_id = media["file_id"]

    title = media["title"]

    media_type = media["type"]

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
#                   BUTTON SYSTEM
# =====================================================

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

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

    # COLLECTION PASSWORD
    if data == "collection_password":

        context.user_data["waiting_password"] = True

        await query.message.reply_text(

            "🔒 Enter Collection Password"

        )

        return

    # CATEGORY
    category = data.split("_")[0]

    index = int(data.split("_")[1])

    await send_media(query, category, index)

# =====================================================
#                 PASSWORD SYSTEM
# =====================================================

async def text_system(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text.lower()

    # PASSWORD CHECK
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

                "✅ Password Correct",

                reply_markup=InlineKeyboardMarkup(keyboard)

            )

        else:

            await update.message.reply_text(

                "❌ Wrong Password"

            )

        return

    # =================================================
    # SMART SEARCH
    # =================================================

    all_titles = []

    media_map = {}

    for category in DATABASE:

        for media in DATABASE[category]:

            title = media["title"]

            all_titles.append(title)

            media_map[title] = media

    # Exact Search
    results = []

    for title in all_titles:

        if text in title.lower():

            results.append(title)

    # Smart Search
    if not results:

        close = get_close_matches(

            text,

            [t.lower() for t in all_titles],

            n=5,

            cutoff=0.4

        )

        for c in close:

            for original in all_titles:

                if original.lower() == c:

                    results.append(original)

    # NO RESULT
    if not results:

        await update.message.reply_text(

            "❌ No Media Found"

        )

        return

    # SEND RESULT
    for title in results:

        media = media_map[title]

        file_id = media["file_id"]

        media_type = media["type"]

        # VIDEO
        if media_type == "video":

            await update.message.reply_video(

                video=file_id,

                caption=f"🎬 {title}"

            )

        # PHOTO
        elif media_type == "photo":

            await update.message.reply_photo(

                photo=file_id,

                caption=f"🖼 {title}"

            )

        # DOCUMENT
        else:

            await update.message.reply_document(

                document=file_id,

                caption=f"📁 {title}"

            )

# =====================================================
#                  FILE ID GETTER
# =====================================================

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # VIDEO
    if update.message.video:

        await update.message.reply_text(

            f"🎬 VIDEO FILE ID 👇\n\n{update.message.video.file_id}"

        )

    # PHOTO
    elif update.message.photo:

        await update.message.reply_text(

            f"🖼 PHOTO FILE ID 👇\n\n{update.message.photo[-1].file_id}"

        )

    # DOCUMENT
    elif update.message.document:

        await update.message.reply_text(

            f"📁 DOCUMENT FILE ID 👇\n\n{update.message.document.file_id}"

        )

# =====================================================
#                    MAIN APP
# =====================================================

app = Application.builder().token(TOKEN).build()

# START
app.add_handler(CommandHandler("start", start))

# BUTTONS
app.add_handler(CallbackQueryHandler(buttons))

# SEARCH + PASSWORD
app.add_handler(

    MessageHandler(

        filters.TEXT & ~filters.COMMAND,

        text_system

    )

)

# FILE ID GETTER
app.add_handler(

    MessageHandler(

        filters.VIDEO |
        filters.PHOTO |
        filters.Document.ALL,

        get_file_id

    )

)

print("✅ Premium Smart Media Bot Running...")

# =====================================================
#                     RUN BOT
# =====================================================

app.run_polling()
