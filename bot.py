import telebot
from telebot import types
import json
from decouple import config

TOKEN = config('TOKEN')
bot = telebot.TeleBot(TOKEN)

with open("content.json", "r") as content:
    content_json = content.read()

welcome = json.loads(content_json)["welcome"]

start_button = types.InlineKeyboardButton('get started to download new music! 🚀', callback_data='song_name')
keyboard = types.InlineKeyboardMarkup()
keyboard.add(start_button)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, welcome, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "song_name":
        bot.send_message(call.message.chat.id, 'good, at first send me a song name in a format: \n\n artist - song_name')

@bot.message_handler(commands=['help'])
def help_message(message):
	bot.reply_to(message, "/start - start to find and download new music\n/help - the command list")

@bot.message_handler(func=lambda message: True)
def incorrect_message_handler(message):
	bot.reply_to(message, "*i don't get it.* if you need help, enter /help", parse_mode='Markdown')

bot.infinity_polling()