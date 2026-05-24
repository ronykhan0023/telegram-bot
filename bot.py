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

from pymongo import MongoClient
from fuzzywuzzy import fuzz

import os

# =====================================================
#                     BOT TOKEN
# =====================================================

TOKEN = "8971545585:AAGAVBOLz_epIWnWwj1IQT_viSBp2thdumk"

# =====================================================
#                  MONGODB SYSTEM
# =====================================================

MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(MONGO_URL)

db = client["telegram_bot"]

media_collection = db["media"]

users_collection = db["users"]

# =====================================================
#                COLLECTION PASSWORD
# =====================================================

COLLECTION_PASSWORD = "20200"

# =====================================================
#                  SAVE USER
# =====================================================

def save_user(user_id):

    exists = users_collection.find_one({
        "user_id": user_id
    })

    if not exists:

        users_collection.insert_one({
            "user_id": user_id
        })

# =====================================================
#                   MAIN MENU
# =====================================================

def main_menu():

    keyboard = [

        [InlineKeyboardButton("🎭 Natok", callback_data="natok_0")],

        [InlineKeyboardButton("🎬 Movie", callback_data="movie_0")],

        [InlineKeyboardButton("😁 Collection", callback_data="collection_lock")],

        [InlineKeyboardButton("🖼 Photo", callback_data="photo_0")],

        [InlineKeyboardButton("🎮 Game", callback_data="game_0")],

        [InlineKeyboardButton("💻 Software", callback_data="software_0")]

    ]

    return InlineKeyboardMarkup(keyboard)

# =====================================================
#                     START
# =====================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    save_user(update.effective_user.id)

    text = """
🎬 Welcome To Video Collection 🎬

━━━━━━━━━━━━━━━━━━

🔥 Professional MongoDB Bot

✅ Auto Upload
✅ Smart Search
✅ MongoDB Database
✅ Permanent Storage
✅ Next / Previous
✅ Password Collection
✅ Unlimited Upload

━━━━━━━━━━━━━━━━━━

👇 Select Category
"""

    await update.message.reply_text(

        text,

        reply_markup=main_menu()

    )

# =====================================================
#                  USER COUNT
# =====================================================

async def users(update: Update, context: ContextTypes.DEFAULT_TYPE):

    total_users = users_collection.count_documents({})

    await update.message.reply_text(

        f"👥 Total Users: {total_users}"

    )

# =====================================================
#                BUTTON SYSTEM
# =====================================================

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    data = query.data

    # =================================================
    # BACK BUTTON
    # =================================================

    if data == "back":

        await query.message.reply_text(

            "🔙 Main Menu",

            reply_markup=main_menu()

        )

        return

    # =================================================
    # COLLECTION LOCK
    # =================================================

    if data == "collection_lock":

        context.user_data["waiting_password"] = True

        await query.message.reply_text(

            "🔒 Enter Collection Password"

        )

        return

    # =================================================
    # CATEGORY
    # =================================================

    category = data.split("_")[0]

    index = int(data.split("_")[1])

    media_list = list(

        media_collection.find({
            "category": category
        })

    )

    if len(media_list) == 0:

        await query.message.reply_text(

            "❌ No Media Found"

        )

        return

    if index >= len(media_list):

        index = 0

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
#                 SEARCH SYSTEM
# =====================================================

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message:
        return

    text = update.message.text.lower()

    # =================================================
    # PASSWORD SYSTEM
    # =================================================

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

    # =================================================
    # SEARCH DATABASE
    # =================================================

    media_list = list(media_collection.find())

    results = []

    for media in media_list:

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

    await update.message.reply_text(

        f"🔍 Found {len(results)} Result"

    )

    for media in results:

        file_id = media["file_id"]

        title = media["title"]

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
#                FILE ID GETTER
# =====================================================

async def file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message:
        return

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
#               AUTO UPLOAD SYSTEM
# =====================================================

async def auto_upload(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:

        if not update.channel_post:
            return

        post = update.channel_post

        caption = post.caption or "No Title"

        lower_caption = caption.lower()

        # =================================================
        # CATEGORY DETECTION
        # =================================================

        category = "movie"

        if "natok" in lower_caption:

            category = "natok"

        elif "collection" in lower_caption:

            category = "collection"

        elif "photo" in lower_caption:

            category = "photo"

        elif "game" in lower_caption:

            category = "game"

        elif "software" in lower_caption:

            category = "software"

        media = None

        # =================================================
        # VIDEO
        # =================================================

        if post.video:

            media = {

                "file_id": post.video.file_id,

                "title": caption,

                "type": "video",

                "category": category

            }

        # =================================================
        # PHOTO
        # =================================================

        elif post.photo:

            media = {

                "file_id": post.photo[-1].file_id,

                "title": caption,

                "type": "photo",

                "category": category

            }

        # =================================================
        # DOCUMENT
        # =================================================

        elif post.document:

            media = {

                "file_id": post.document.file_id,

                "title": caption,

                "type": "document",

                "category": category

            }

        # =================================================
        # SAVE TO MONGODB
        # =================================================

        if media:

            exists = media_collection.find_one({

                "file_id": media["file_id"]

            })

            if not exists:

                media_collection.insert_one(media)

                print(f"✅ Saved → {category}")

            else:

                print("⚠ Already Exists")

    except Exception as e:

        print("AUTO UPLOAD ERROR:", e)

# =====================================================
#                    MAIN APP
# =====================================================

app = Application.builder().token(TOKEN).build()

# START
app.add_handler(CommandHandler("start", start))

# USERS
app.add_handler(CommandHandler("users", users))

# BUTTONS
app.add_handler(CallbackQueryHandler(button))

# SEARCH
app.add_handler(

    MessageHandler(

        filters.TEXT & ~filters.COMMAND,

        search

    )

)

# FILE ID GETTER
app.add_handler(

    MessageHandler(

        filters.VIDEO |

        filters.PHOTO |

        filters.Document.ALL,

        file_id

    )

)

# AUTO UPLOAD
app.add_handler(

    MessageHandler(

        filters.ALL,

        auto_upload

    )

)

print("✅ MongoDB Professional Bot Running...")

app.run_polling(

    drop_pending_updates=True,

    allowed_updates=Update.ALL_TYPES,

    close_loop=False

)
