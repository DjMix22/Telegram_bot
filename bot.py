import telebot

n = 0

token = '6629484918:AAFcOI22QsRk9nFwlZC1euNGtItL0IFBqZk'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['spam'])
def main(message, n=0):
    while True:
        n += 1
        bot.send_message(message.chat.id, str(n))


bot.polling(none_stop=True)
