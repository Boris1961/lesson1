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
    bot_command=update.message.text
    bot.sendMessage(update.message.chat_id, calc(bot_command))


def calc(exp_s):
    for s in "+-*/":
        opr=s
        opns=exp_s.split(s)
        if len(opns)==2:
            opn1=opns[0]
            opn2=opns[1]
            for n in range(0, len(opn1)-1):
                if "0123456789".find(opn1[n])==-1:
                    return "Error"
            for n in range(0, len(opn2)-1):
                if "0123456789".find(opn2[n])==-1:
                    return "Error"
            opn1=int(opn1)
            opn2=int(opn2)
            if opr=="+":
                return str(opn1+opn2)
            elif opr=="-":
                return str(opn1-opn2)
            elif opr=="/":
                if opn2==0:
                    return "Error: деление на ноль."
                return str(opn1/opn2)
            elif opr=="*":
                return str(opn1*opn2)

    return "Error"            
  

if __name__ == '__main__':
    main()
