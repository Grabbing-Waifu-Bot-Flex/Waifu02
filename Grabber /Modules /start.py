@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
     await query.message.reply_photo(
            photo="http://telegra.ph/file/4beb984109631f88704b8.jpg",
            caption=" Welcome To The World of Solo Leveling                          What are you in The World Of Solo Leveling",  reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Hunter", callback_data="hun"),
                InlineKeyboardButton("Healer", callback_data="heal")
            ]
        ]
    ))
elif data == "hun":
        await query.message.reply_photo(
            photo="http://telegra.ph/file/9471582944eb83307d974.jpg", caption You Have Choosen Hunter Section  Which Starter Hunter You Choose", reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Cho Kyuhwan", callback_data="cho"),
                InlineKeyboardButton("Yoo Jino", callback_data="yoo"),
        InlineKeyboardButton("Kim Sangshik", callback_data="kim")    
     ]
        ]
    ))
elif data =="cho"
       await query.message.reply_photo(photo = "http://telegra.ph/file/3f1e94cdd6af9da9e3e33.jpg",caption = " Type > Mage
Rank > C

Strength : 55
Agility : 65
Stamina : 50
Intelligence : 35
Perception: 45", reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("confirm", callback_data="con_cho"),
                InlineKeyboardButton("Decline", callback_data="decline_cho")
            ]
        ]
    ))

elif data =="yoo"
       await query.message.reply_photo(photo = "http://telegra.ph/file/4aa0e5aa4c70aef98cce6.jpg",caption = " Type > Tank
Rank > D

Strength : 50
Agility : 39
Stamina : 60
Intelligence : 30
Perception: 40", reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("confirm", callback_data="con_yoo"),
                InlineKeyboardButton("Decline", callback_data="decline_yoo")
            ]
        ]
    ))

elif data =="kim"
       await query.message.reply_photo(photo = "http://telegra.ph/file/76beb67d46691ac83527d.jpg",caption = " Type > Assasin
Rank > D

Strength : 60
Agility : 50
Stamina : 45
Intelligence : 45
Perception: 40", reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("confirm", callback_data="con_kim"),
                InlineKeyboardButton("Decline", callback_data="decline_kim")
            ]
        ]
    ))
elif data =="con_cho"
await query.message.reply_photo(photo="http://telegra.ph/file/3f1e94cdd6af9da9e3e33.jpg" caption="Hunter Cho Kyuhwan Has Been Added To Your /huntervault")

elif data =="decline_cho" 
await query.message.edit_text("If you Don't need This Hunter Do /start to Get New Hunter Details")

elif data =="con_yoo"
await query.message.reply_photo(photo="http://telegra.ph/file/4aa0e5aa4c70aef98cce6.jpg" caption="Hunter Yoo Jino  Has Been Added To Your /huntervault")

elif data =="decline_yoo" 
await query.message.edit_text("If you Don't need This Hunter Do /start to Get New Hunter Details")

elif data =="con_kim"
await query.message.reply_photo(photo="http://telegra.ph/file/76beb67d46691ac83527d.jpg" caption="Hunter Kim Sangshik Has Been Added To Your /huntervault")

elif data =="decline_kim" 
await query.message.edit_text("If you Don't need This Hunter Do /start to Get New Hunter Details")