import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your bot's API token
API_TOKEN = '7249088154:AAGIJtpUgBey0WTzr33Ul4qOWcn0RoHz2gY'
YOUR_CHAT_ID = '6771179717'  # Replace with your Telegram user ID

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)  # Change to DEBUG to get more detailed logs

logger = logging.getLogger(__name__)

# Define start command handler
async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("ѕυвмιт αѕѕιgηмєηт", callback_data='submit_assignment')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('𝗛𝗶! 𝗪𝗵𝗮𝘁 𝗱𝗼 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝗧𝗼𝗱𝗮𝘆?', reply_markup=reply_markup)

# Define help command handler
async def help_command(update: Update, context: CallbackContext) -> None:
    help_message = "𝗖𝗵𝗼𝗼𝘀𝗲 𝘄𝗵𝗼 𝘁𝗼 𝗰𝗼𝗺𝗺𝘂𝗻𝗶𝗰𝗮𝘁𝗲 𝘄𝗶𝘁𝗵:\n\n"
    help_message += "C𝖍𝖎𝖊𝖋 L𝖊𝖆𝖉𝖊𝖗𝖘:\n"
    help_message += "1. [Uncle Kanan](https://wa.me/255748100268)\n"
    help_message += "2. [Aneth Alphonce](https://wa.me/255747163173)\n\n"
    help_message += "P𝖆𝖗𝖊𝖓𝖙𝖘 H𝖚𝖇:\n"
    help_message += "1. [Miss Happie](https://wa.me/255759035364)\n"
    help_message += "2. [Square Mahad](https://wa.me/255672330843)\n"
    help_message += "3. [Madam Lindael](https://wa.me/255676441828)\n"
    help_message += "4. [Ch13f mz1ngw4](https://wa.me/255714103334)\n"
    help_message += "5. [Blissed Sia](https://wa.me/255624356355)\n"
    help_message += "6. [He is Ndele](https://wa.me/255742255142)\n"
    help_message += "7. [Jorvenmetili](https://wa.me/255624586290)\n"
    help_message += "8. [Mentor Michael](https://wa.me/255786483514)\n"
    help_message += "9. [Bro. Sharif](https://wa.me/255717173871)\n"
    help_message += "10. [Sheikh Omary](https://wa.me/255746867505)\n"
    
    # Escape the dot character in the markdown links
    help_message = help_message.replace(".", "\.")
    
    await update.message.reply_text("𝑴𝒆𝒆𝒕 *𝐂𝐬 𝐆𝐚𝐥𝐚𝐱𝐲 𝐓𝐞𝐚𝐦* 𝒇𝒐𝒓 𝒂𝒔𝒔𝒊𝒔𝒕𝒂𝒏𝒄𝒆\n" + help_message, parse_mode='MarkdownV2')

# Define home command handler
async def home_command(update: Update, context: CallbackContext) -> None:
    await start(update, context)

# Define community command handler
async def community_command(update: Update, context: CallbackContext) -> None:
    community_link = 'https://chat.whatsapp.com/C6sxdW6jlDt6ifOUrxDV1W'
    await update.message.reply_text(f'𝗝𝗼𝗶𝗻 𝗼𝘂𝗿 𝗰𝗼𝗺𝗺𝘂𝗻𝗶𝘁𝘆 𝗼𝗻 𝗪𝗵𝗮𝘁𝘀𝗔𝗽𝗽: [Click here]({community_link})', parse_mode='MarkdownV2')

# Define file handler
async def handle_file(update: Update, context: CallbackContext) -> None:
    file = update.message.document
    if file:
        await context.bot.send_document(chat_id=YOUR_CHAT_ID, document=file.file_id, caption=f'File from {update.message.from_user.username}')
        await update.message.reply_text('𝗔𝘀𝘀𝗶𝗴𝗻𝗺𝗲𝗻𝘁 𝗿𝗲𝗰𝗲𝗶𝘃𝗲𝗱 𝗮𝗻𝗱 𝘀𝘂𝗯𝗺𝗶𝘁𝘁𝗲𝗱 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆, 𝗛𝗮𝘃𝗲 𝗮 𝗻𝗶𝗰𝗲 𝘁𝗶𝗺𝗲!')

# Define contact_cr command handler
async def contact_cr(update: Update, context: CallbackContext) -> None:
    whatsapp_link = 'https://wa.me/255748100268'
    await update.message.reply_text(f'*Contact CR directly on WhatsApp*: [Click here]({whatsapp_link})', parse_mode='MarkdownV2')

# Define callback query handler
async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    
    if query.data == 'submit_assignment':
        await query.edit_message_text(text="𝗬𝗼𝘂 𝘀𝗲𝗹𝗲𝗰𝘁𝗲𝗱 𝘁𝗼 𝘀𝘂𝗯𝗺𝗶𝘁 𝘁𝗵𝗲 𝗮𝘀𝘀𝗶𝗴𝗻𝗺𝗲𝗻𝘁, 𝗣𝗹𝗲𝗮𝘀𝗲 𝘂𝗽𝗹𝗼𝗮𝗱 𝘆𝗼𝘂𝗿 𝗮𝘀𝘀𝗶𝗴𝗻𝗺𝗲𝗻𝘁")

def main():
    application = Application.builder().token(API_TOKEN).build()
    
    # Register handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('home', home_command))
    application.add_handler(CommandHandler('community', community_command))
    application.add_handler(MessageHandler(filters.Document.ALL, handle_file))
    application.add_handler(CommandHandler('contact_cr', contact_cr))
    application.add_handler(CallbackQueryHandler(button))
    
    # Set bot commands
    commands = [
        BotCommand("start", "Start the bot"),
        BotCommand("help", "Contact admin"),
        BotCommand("home", "Go to home"),
        BotCommand("community", "Join community"),
        BotCommand("contact_cr", "Contact CR")
    ]
    application.bot.set_my_commands(commands)

    # Start the Bot
    print("Starting bot")
    application.run_polling()

if __name__ == '__main__':
    main()
