from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackContext, CallbackQueryHandler
from Grabber import application, user_collection

# Replace OWNER_ID with the actual owner's user ID
OWNER_ID = 6584789596

async def transfer(update: Update, context: CallbackContext):
    try:
        # Check if the user is the owner
        user_id = update.effective_user.id
        if user_id != OWNER_ID:
            await update.message.reply_text('You are not authorized to use this command.')
            return

        # Ensure the command has the correct number of arguments
        if len(context.args) != 2:
            await update.message.reply_text('Please provide two valid user IDs for the transfer.')
            return

        sender_id = int(context.args[0])
        receiver_id = int(context.args[1])

        # Retrieve sender's and receiver's information
        sender = await user_collection.find_one({'id': sender_id})
        receiver = await user_collection.find_one({'id': receiver_id})

        # Check if both sender and receiver exist
        if not sender:
            await update.message.reply_text(f'Sender with ID {sender_id} not found.')
            return

        if not receiver:
            await update.message.reply_text(f'Receiver with ID {receiver_id} not found.')
            return

        # Create confirmation buttons
        buttons = [
            [InlineKeyboardButton("Yes, Transfer", callback_data=f"transfer_yes_{sender_id}_{receiver_id}"),
             InlineKeyboardButton("No, Cancel", callback_data="transfer_no")]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)

        # Send confirmation message
        await update.message.reply_text(
            f"Are you sure you want to transfer all characters from user {sender_id} to user {receiver_id}?",
            reply_markup=reply_markup
        )

    except ValueError:
        await update.message.reply_text('Invalid User IDs provided.')

# Callback function to handle the user's response
async def handle_transfer_confirmation(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    if query.data.startswith("transfer_yes_"):
        sender_id, receiver_id = map(int, query.data.split("_")[2:])

        try:
            # Transfer waifus from sender to receiver
            receiver_waifus = await user_collection.find_one({'id': receiver_id})
            if receiver_waifus is None:
                receiver_waifus = []
            receiver_waifus.extend(await user_collection.find_one({'id': sender_id}).get('characters', []))

            await user_collection.update_one({'id': receiver_id}, {'$set': {'characters': receiver_waifus}})
            await user_collection.update_one({'id': sender_id}, {'$set': {'characters': []}})

            await query.edit_message_text("All characters transferred successfully!")
        except Exception as e:
            await query.edit_message_text(f"An error occurred while transferring: {str(e)}")

    elif query.data == "transfer_no":
        await query.edit_message_text("Transfer cancelled.")

# Register the command handler and the callback query handler
application.add_handler(CommandHandler("transfer", transfer))
application.add_handler(CallbackQueryHandler(handle_transfer_confirmation, pattern="^transfer_"))