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
def sendWelcomeMessage(message):
    msg = "Добрый день, "+message.from_user.first_name
    markup = types.ReplyKeyboardMarkup()
    okButton = types.KeyboardButton('Начать заказывать')
    markup.add(okButton)
    bot.send_message(message.chat.id, msg,reply_markup=markup)


@bot.message_handler(func=lambda m: True) # Handler for messages
def send_messages(message):
    if(message.text == 'Начать заказывать'):
        markup = types.ReplyKeyboardMarkup(row_width=3)
        menuBtn = types.KeyboardButton('Меню')
        basketBtn = types.KeyboardButton('Корзина')
        orderBtn = types.KeyboardButton('Оформить заказ')
        aboutBtn = types.KeyboardButton('О нас')
        myOrdersBtn = types.KeyboardButton('Мои заказы')
        callBtn = types.KeyboardButton('Связаться с менеджером')
        markup.add(menuBtn)
        markup.add(basketBtn)
        markup.add(orderBtn)
        markup.add(myOrdersBtn)
        markup.add(callBtn)
        bot.send_message(message.chat.id, 'Отлично! Приятного пользования!',reply_markup=markup)
    elif(message.text =='Меню'):
        url='https://img.povar.ru/uploads/e6/32/6e/0e/vanilnii_latte-645351.JPG'
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Добавить в корзину", callback_data="addToCartLatte")
        keyboard.add(callback_button)
        bot.send_photo(message.chat.id, url,caption ='Латте',reply_markup=keyboard)
    elif(message.text == 'Корзина'):
        print(basket)
        
@bot.callback_query_handler(func=lambda call: True) # Handler for queries
def menu(call):
    if call.data=="addToCartLatte":
        small = types.InlineKeyboardButton(text="300 Мл", callback_data="small_latte")
        medium = types.InlineKeyboardButton(text="400 Мл", callback_data="medium_latte")
        large = types.InlineKeyboardButton(text="500 Мл", callback_data="large_latte")
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(small)
        keyboard.add(medium)
        keyboard.add(large)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='Латте \nВыберите размер:\n',reply_markup = keyboard)
    if call.data == "small_latte":
        amount = types.InlineKeyboardMarkup()
        for i in range(1, 10):
            amount.add(types.InlineKeyboardButton(text=i, callback_data=i))
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='Латте \nВыберите количество:\n',reply_markup = amount)
        
if __name__ == '__main__':
    bot.infinity_polling()


    





