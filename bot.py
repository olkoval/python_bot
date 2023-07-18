import telebot;

bot = telebot.TeleBot('6143440693:AAH4bP2Qjwr_zWNfIzpWqSvOEDDcW3YMCok');
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    text = message.text.split();
    co = len(text);
    if co >= 2:
        text.reverse();
        bot.send_message(message.from_user.id," ".join(text))
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Строка должна содержать два или больше слова")
    else:
        bot.send_message(message.from_user.id, "Строка должна содержать два или больше слова")
bot.polling(none_stop=True, interval=0)
