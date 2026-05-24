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

import json

# =====================================================
#                     BOT TOKEN
# =====================================================

TOKEN = "8971545585:AAHNJGwWJbzgEofYTd5qEJ4CQBpjCXkbksg"

# =====================================================
#               COLLECTION PASSWORD
# =====================================================

COLLECTION_PASSWORD = "20200"

# =====================================================
#                 SAVE USER SYSTEM
# =====================================================

def save_user(user_id):

    with open("users.json", "r") as file:

        users = json.load(file)

    if user_id not in users:

        users.append(user_id)

        with open("users.json", "w") as file:

            json.dump(users, file)

# =====================================================
#                    LOAD DATABASE
# =====================================================

def load_database():

    with open("database.json", "r") as file:

        return json.load(file)

# =====================================================
#                    SAVE DATABASE
# =====================================================

def save_database(data):

    with open("database.json", "w") as file:

        json.dump(data, file, indent=4)

# =====================================================
#                     START MENU
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

🔥 Professional Media Bot

✅ Natok
✅ Movie
✅ Collection
✅ Photos
✅ Games
✅ Software

━━━━━━━━━━━━━━━━━━

🔍 Smart Search Enabled
⚡ Auto Upload Enabled
🔐 Collection Password Enabled

━━━━━━━━━━━━━━━━━━

👇 Select Category
"""

    await update.message.reply_text(
        text,
        reply_markup=reply_markup
    )

# =====================================================
#                     USER COUNT
# =====================================================

async def users(update: Update, context: ContextTypes.DEFAULT_TYPE):

    with open("users.json", "r") as file:

        users = json.load(file)

    await update.message.reply_text(
        f"👥 Total Users: {len(users)}"
    )

# =====================================================
#                    BUTTON SYSTEM
# =====================================================

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    data = query.data

    db = load_database()

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

    # =================================================
    # COLLECTION PASSWORD
    # =================================================

    elif data == "collection_lock":

        context.user_data["waiting_for_password"] = True

        await query.message.reply_text(
            """
🔒 Collection Locked

📌 Enter Password
"""
        )

    # =================================================
    # CATEGORY SYSTEM
    # =================================================

    else:

        category = data.split("_")[0]

        index = int(data.split("_")[1])

        media_list = db.get(category, [])

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
#                 SEARCH SYSTEM
# =====================================================

async def search_system(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text.lower()

    # PASSWORD SYSTEM
    if context.user_data.get("waiting_for_password"):

        password = update.message.text

        if password == COLLECTION_PASSWORD:

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
                """
✅ Password Correct

🔓 Collection Unlocked
""",
                reply_markup=reply_markup
            )

        else:

            await update.message.reply_text(
                "❌ Wrong Password"
            )

        return

    # =================================================
    # SEARCH DATABASE
    # =================================================

    db = load_database()

    results = []

    for category in db:

        for media in db[category]:

            score = fuzz.partial_ratio(
                text,
                media["title"].lower()
            )

            if score > 70:

                results.append(media)

    # =================================================
    # NO RESULT
    # =================================================

    if len(results) == 0:

        await update.message.reply_text(
            "❌ No Result Found"
        )

        return

    # =================================================
    # SEND RESULT
    # =================================================

    await update.message.reply_text(
        f"🔍 Found {len(results)} Result"
    )

    for media in results:

        file_id = media["file_id"]

        title = media["title"]

        file_type = media["type"]

        # VIDEO
        if file_type == "video":

            await update.message.reply_video(
                video=file_id,
                caption=f"🎬 {title}"
            )

        # PHOTO
        elif file_type == "photo":

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
#                AUTO UPLOAD SYSTEM
# =====================================================

async def auto_upload(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.channel_post:

        db = load_database()

        caption = update.channel_post.caption

        if not caption:

            return

        category = "movie"

        lower_caption = caption.lower()

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

        # VIDEO
        if update.channel_post.video:

            file_id = update.channel_post.video.file_id

            db[category].append({

                "file_id": file_id,
                "title": caption,
                "type": "video"

            })

        # PHOTO
        elif update.channel_post.photo:

            file_id = update.channel_post.photo[-1].file_id

            db[category].append({

                "file_id": file_id,
                "title": caption,
                "type": "photo"

            })

        # DOCUMENT
        elif update.channel_post.document:

            file_id = update.channel_post.document.file_id

            db[category].append({

                "file_id": file_id,
                "title": caption,
                "type": "document"

            })

        save_database(db)

# =====================================================
#                     MAIN SYSTEM
# =====================================================

app = Application.builder().token(TOKEN).build()

# START
app.add_handler(CommandHandler("start", start))

# USER COUNT
app.add_handler(CommandHandler("users", users))

# BUTTON
app.add_handler(CallbackQueryHandler(button))

# SEARCH + PASSWORD
app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        search_system
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

# AUTO UPLOAD
app.add_handler(
    MessageHandler(
        filters.ALL,
        auto_upload
    )
)

print("✅ Advanced Professional Bot Running...")

app.run_polling(
    allowed_updates=Update.ALL_TYPES
)