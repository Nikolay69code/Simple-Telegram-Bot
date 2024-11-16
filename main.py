import webbrowser

import telebot
import config
import random
from telebot import types

token = "7671552008:AAEHzK5BrfRqwigEXvX4wy8G-gAPTxxkCmc"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start','main','hallo','привет'])
def welcome(message):
    sti = open('AnimatedSticker.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id,f"<b>Привет</b> {message.from_user.first_name}, <em><u>я ваш бот-помошник Джей!</u></em>",parse_mode="html")
    bot.send_message(message.chat.id,f"<b>Ваш username = </b> {message.from_user.username}",parse_mode="html")
@bot.message_handler(commands=['help','помощь'])
def welcome(message):
    sti = open('AnimatedSticker.tgs', 'rb')
    bot.send_message(message.chat.id,message)

@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open("https://scratch.mit.edu/projects/1097378306/editor")

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Перейти на сайт",url = "https://scratch.mit.edu/projects/1097378306/editor")
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton("Удалить фото", callback_data='delete')
    markup.row(btn2,btn3)
    bot.reply_to(message,"Какое красивое фото!",reply_markup = markup)

@bot.callback_query_handler(func=lambda callback:True)
def call_back_message(callback):
    if callback.data == "delete":
        bot.delete_message(callback.message.chat.id, callback.message.message_id-1)

bot.polling(none_stop=True)