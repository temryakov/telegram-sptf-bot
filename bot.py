import telebot
from telebot import types
from classes_bot import JSONReader, Validation
from decouple import config

TOKEN = config('TOKEN')
bot = telebot.TeleBot(TOKEN)

jsn = JSONReader()
validate = Validation()

ask_for_a_song_name = jsn.readContent("song_name", "ask_for_a_song_name")
help_info = jsn.readContent("other", "help_message")
incorrect_message = jsn.readContent("other", "incorrect_message")

def error(message):
	return bot.send_message(message.chat.id, incorrect_message, parse_mode='Markdown')

# welcome message

@bot.message_handler(commands=['start'])
def send_welcome(message):
	welcome = jsn.readContent("start_message", "welcome")

	start_button = types.InlineKeyboardButton('Get started to download new music! 🚀', callback_data='song_name')
	keyboard = types.InlineKeyboardMarkup()
	keyboard.add(start_button)

	bot.reply_to(message, welcome, reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help_message(message):
	bot.reply_to(message, help_info, parse_mode='Markdown')

@bot.message_handler(commands=['download'])
def find_music(message):
    bot.reply_to(message, ask_for_a_song_name, parse_mode='Markdown')

# ask for a song name, if user pressed the button

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "song_name":			
        bot.send_message(call.message.chat.id, ask_for_a_song_name, parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def message_receiver(message):
	if ' - ' in message.text:	
		song_name = validate.song_name(message.text)
		bot.send_message(message.chat.id, song_name, parse_mode='Markdown')

	else:
		error(message)


bot.infinity_polling()