import telebot
import parser
import re

from telebot import types


#main variables
TOKEN = "1269042254:AAGZp7XwcegtFPdXD2vBfNZ6u3qCn5-0Pzk"
bot = telebot.TeleBot(TOKEN)	#create a new Telegram Bot object

global basket
basket = []



@bot.message_handler(commands=['start'])
def any_msg(message):
    url='https://img.povar.ru/uploads/e6/32/6e/0e/vanilnii_latte-645351.JPG'
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Добавить в корзину", callback_data="addToCartLatte")
    keyboard.add(callback_button)
    bot.send_photo(message.chat.id, url,caption ='Латте',reply_markup=keyboard)


    
@bot.callback_query_handler(func=lambda call: True)
def longname(call):
    bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id,caption='Латте добавлен в корзину')
    if call.data == "addToCartLatte":
        basket.append('Латте')
    print(basket)


if __name__ == '__main__':
    bot.infinity_polling()
