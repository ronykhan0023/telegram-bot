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
#                   MONGODB URL
# =====================================================

MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(MONGO_URL)

db = client["telegram_bot"]

media_collection = db["media"]

users_collection = db["users"]

# =====================================================
#              COLLECTION PASSWORD
# =====================================================

COLLECTION_PASSWORD = "20200"

# =====================================================
#                   SAVE USER
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
#                 START COMMAND
# =====================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    save_user(update.effective_user.id)

    keyboard = [

        [InlineKeyboardButton("🎭 Natok", callback_data="natok_0")],

        [InlineKeyboardButton("🎬 Movie", callback_data="movie_0")],

        [InlineKeyboardButton("😁 Collection", callback_data="collection_lock")],

        [InlineKeyboardButton("🖼 Photo", callback_data="photo_0")],

        [InlineKeyboardButton("🎮 Game", callback_data="game_0")],

        [InlineKeyboardButton("💻 Software", callback_data="software_0")]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    text = """
🎬 Welcome To Video Collection 🎬

━━━━━━━━━━━━━━━━━━

🔥 Professional MongoDB Bot

✅ Permanent Storage
✅ Auto Upload
✅ Smart Search
✅ Password Collection
✅ Unlimited Upload
✅ MongoDB Database

━━━━━━━━━━━━━━━━━━

👇 Select Category
"""

    await update.message.reply_text(

        text,

        reply_markup=reply_markup

    )

# =====================================================
#                  USERS COUNT
# =====================================================

async def users(update: Update, context: ContextTypes.DEFAULT_TYPE):

    total_users = users_collection.count_documents({})

    await update.message.reply_text(

        f"👥 Total Users: {total_users}"

    )

# =====================================================
#                CATEGORY BUTTON
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

            [InlineKeyboardButton("😁 Collection", callback_data="collection_lock")],

            [InlineKeyboardButton("🖼 Photo", callback_data="photo_0")],

            [InlineKeyboardButton("🎮 Game", callback_data="game_0")],

            [InlineKeyboardButton("💻 Software", callback_data="software_0")]

        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.message.reply_text(

            "🔙 Main Menu",

            reply_markup=reply_markup

        )

        return

    # =================================================
    # COLLECTION PASSWORD
    # =================================================

    if data == "collection_lock":

        context.user_data["waiting_for_password"] = True

        await query.message.reply_text(

            "🔒 Enter Collection Password"

        )

        return

    # =================================================
    # CATEGORY MEDIA
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

    media = media_list[index]

    keyboard = []

    if index > 0:

        keyboard.append(

            InlineKeyboardButton(

                "⏮ Previous",

                callback_data=f"{category}_{index-1}"

            )

        )

    if index < len(media_list) - 1:

        keyboard.append(

            InlineKeyboardButton(

                "⏭ Next",

                callback_data=f"{category}_{index+1}"

            )

        )

    nav_buttons = [keyboard]

    nav_buttons.append(

        [InlineKeyboardButton("🔙 Back", callback_data="back")]

    )

    reply_markup = InlineKeyboardMarkup(nav_buttons)

    file_id = media["file_id"]

    title = media["title"]

    file_type = media["type"]

    # VIDEO
    if file_type == "video":

        await query.message.reply_video(

            video=file_id,

            caption=f"🎬 {title}",

            reply_markup=reply_markup

        )

    # PHOTO
    elif file_type == "photo":

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
#                SEARCH SYSTEM
# =====================================================

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text.lower()

    # PASSWORD
    if context.user_data.get("waiting_for_password"):

        if text == COLLECTION_PASSWORD:

            context.user_data["waiting_for_password"] = False

            keyboard = [

                [

                    InlineKeyboardButton(

                        "🔥 Open Collection",

                        callback_data="collection_0"

                    )

                ]

            ]

            reply_markup = InlineKeyboardMarkup(keyboard)

            await update.message.reply_text(

                "✅ Collection Unlocked",

                reply_markup=reply_markup

            )

        else:

            await update.message.reply_text(

                "❌ Wrong Password"

            )

        return

    # SEARCH
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

        file_type = media["type"]

        if file_type == "video":

            await update.message.reply_video(

                video=file_id,

                caption=f"🎬 {title}"

            )

        elif file_type == "photo":

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

async def file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):

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
#                AUTO UPLOAD SYSTEM
# =====================================================

async def auto_upload(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:

        if not update.channel_post:

            return

        post = update.channel_post

        caption = post.caption or "No Title"

        lower_caption = caption.lower()

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

        # VIDEO
        if post.video:

            media = {

                "file_id": post.video.file_id,

                "title": caption,

                "type": "video",

                "category": category

            }

        # PHOTO
        elif post.photo:

            media = {

                "file_id": post.photo[-1].file_id,

                "title": caption,

                "type": "photo",

                "category": category

            }

        # DOCUMENT
        elif post.document:

            media = {

                "file_id": post.document.file_id,

                "title": caption,

                "type": "document",

                "category": category

            }

        if media:

            media_collection.insert_one(media)

            print(f"✅ Saved In MongoDB → {category}")

    except Exception as e:

        print("AUTO UPLOAD ERROR:", e)

# =====================================================
#                   MAIN SYSTEM
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

# FILE ID
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
