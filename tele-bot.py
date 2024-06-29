from telegram import Update
from telegram.ext import Updater, InlineQueryHandler, CallbackContext, InlineQueryResultArticle, InputTextMessageContent

def inline_query(update: Update, context: CallbackContext):
    query = update.inline_query.query
    if query == "play_game":
        game_url = "hhttps://flappy-ochre.vercel.app/"
        results = [
            InlineQueryResultArticle(
                id="1",
                title="Play Game",
                input_message_content=InputTextMessageContent(game_url)
            )
        ]
        update.inline_query.answer(results)

def main():
    updater = Updater(token='7075835530:AAHlNztDkDNWDbgJTkvgAQ8diUEdUa69Yho', use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(InlineQueryHandler(inline_query))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
