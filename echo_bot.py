import telebot
from decouple import config

TOKEN = config('TOKEN')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "hi, due to sanctions spotify has leave russia however demand for good music still persists so i can help you get started to listen and download new music \n\n at first, send me name of track with a hyphen")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()