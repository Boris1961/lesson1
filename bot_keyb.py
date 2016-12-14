import telegram.ext

custom_keyboard = [['top-left', 'top-right'], ['bottom-left', 'bottom-right']]
reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
bot.sendMessage(chat_id=chat_id, text="Custom Keyboard Test", reply_markup=reply_markup)
