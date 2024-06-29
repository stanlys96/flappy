from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Define a start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to my game! Type /play to start.')

# Define a play command handler
def play(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Game started! Here are the rules...')

def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater("7075835530:AAHlNztDkDNWDbgJTkvgAQ8diUEdUa69Yho")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("play", play))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT.
    updater.idle()

if __name__ == '__main__':
    main()
