import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultPhoto, ParseMode, Update
from telegram.ext import Application, InlineQueryHandler, ApplicationBuilder, ContextTypes

async def inlinequery(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the inline query."""
    query = update.inline_query.query
    results = []
    next_offset = update.inline_query.offset
    
    if not query:
        return 

    # Assuming you have a function to retrieve the character data
    character = await get_character_data(query) 

    if not character:
        return 

    # Example of retrieving top collectors
    top_collectors = await get_top_collectors(character['id']) 

    global_count = await get_global_count(character['id']) 

    caption = f"<b>Lᴏᴏᴋ Aᴛ Tʜɪs Wᴀɪғᴜ....!!</b>\n\n<b>{character['id']}:</b> {character['name']}\n <b>{character['anime']}</b>\n﹙<b>{character['rarity'][0]} 𝙍𝘼𝙍𝙄𝙏𝙔:</b> {character['rarity'][2:]}﹚\n\n<b>Gʟᴏʙᴀʟʟʏ Gʀᴀʙ {global_count} Times...</b>\n\n<b>Top Collectors:</b>\n"

    # Dynamically add Top Collectors
    for i, (username, count) in enumerate(top_collectors[:3]):
        caption += f"{i+1}. {username} - x{count}\n"

    # Add the inline button at the end
    button = InlineKeyboardButton("GLOBAL GRABBED", callback_data=f'<b>Gʟᴏʙᴀʟʟʏ Gʀᴀʙ {global_count} Times...</b>')
    keyboard = InlineKeyboardMarkup([[button]])

    results.append(
        InlineQueryResultPhoto(
            id=f"{character['id']}_{time.time()}",
            thumbnail_url=character['img_url'],
            photo_url=character['img_url'],
            caption=caption,
            parse_mode=ParseMode.HTML,
            reply_markup=keyboard
        )
    )

    await update.inline_query.answer(results, next_offset=next_offset, cache_time=5)
