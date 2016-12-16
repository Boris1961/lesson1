from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def main(): 
    updater = Updater("312039735:AAFzeUt-LKAnHjr9n58unpfO8_CAsxbCq70")
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("abort", abort_bot))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    updater.start_polling()
    updater.idle()

def greet_user(bot, update):
    print('Вызван /start')
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')

def abort_bot(bot, update):
    print('Вызван /abort')
    bot.sendMessage(update.message.chat_id, text-'ухожу-ухожу-ухожу...')
    exit()

def talk_to_me(bot, update):
    print('Пришло сообщение: {}'.format(update.message.text))
    custom_keyboard = [['top-left', 'top-right'], ['bottom-left', 'bottom-right']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.sendMessage(chat_id=chat_id, text="Custom Keyboard Test", reply_markup=reply_markup)  

if __name__ == '__main__':
    main()
