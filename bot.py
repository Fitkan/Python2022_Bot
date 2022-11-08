import telebot
bot = telebot.TeleBot("5280621901:AAGaq-Io-73IClqgrPYUXW6N_SBz9T_FWiw")

@bot.message_handler(content_types=['text'])
def send_echo(message):
		bot.reply_to(message , message.text)


bot.polling( none_stop = True )