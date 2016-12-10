#  coding: utf-8
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def main(): 
    updater = Updater("312039735:AAFzeUt-LKAnHjr9n58unpfO8_CAsxbCq70")
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    updater.start_polling()
    updater.idle()

def greet_user(bot, update):
    print('Вызван /start')
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')

def talk_to_me(bot, update):
    print('Пришло сообщение: {}'.format(update.message.text))
    UPT=update.message.text
    bot.sendMessage(update.message.chat_id, len(UPT.split()))

if __name__ == '__main__':
    main()