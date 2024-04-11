import telebot
from telebot import types
bot = telebot.TeleBot('6782576467:AAFkhRFicIGxMcyijCdYA8tEjQvEt6NqSgs')
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton('bu yerda shop🛍 bo\'limi bo\'ladi')
    btn1 = types.KeyboardButton('Instagram sahifa📷')
    btn2 = types.KeyboardButton('Telegram kanal🗂')
    btn4 = types.KeyboardButton('YouTube kanal📺')
    btn3 = types.KeyboardButton('Admin bilan bog\'lanish👤')
    markup.add(btn)
    markup.add(btn1, btn2, btn4)
##    markup.add(btn2)
    markup.add(btn3)
    bot.send_message(message.chat.id,f'Assalomu aleykum ! {message.from_user.first_name} <b>Madomoa Brand💚 Hana Advance🌱 Hana brendlarining</b> <u>rasmiy botiga xush kelibsiz</u> !', parse_mode = 'html' , reply_markup=markup)
##----------------------------------------------------------------------------------------------------------------------------------------
@bot.message_handler(func=lambda message: message.text == 'Instagram sahifa📷')
def sahifa(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Instagram sahifa📷', url="https://www.instagram.com/madomoa_brand/")
    markup.add(btn1)
    bot.send_message(message.chat.id, 'Instagram sahifaga o\'tish uchun pastdagi 👇 tugmani bosing !', reply_markup=markup)
##    bot.send_message(message.chat.id, 'Instagram sahifaga o\'tish uchun tugmani bosing')
##-----------------------------------------------------------------------------------------------------------------------------------------
@bot.message_handler(func=lambda message: message.text == 'Telegram kanal🗂')
def kanal(message):
    markup = types.InlineKeyboardMarkup()
    btn2 = types.InlineKeyboardButton('Kanalga o\'tish🗂', url="https://t.me/madomoa_brand")
    markup.add(btn2)
    bot.send_message(message.chat.id, 'Telegram kanalga o\'tish uchun pastdagi 👇 tugmani bosing !', reply_markup=markup)
##    bot.send_message(message.chat.id, 'Telegram kanalga o\'tish uchun tugmani bosing')
##-----------------------------------------------------------------------------------------------------------------------------------------
@bot.message_handler(func=lambda message: message.text == 'YouTube kanal📺')
def kanal(message):
    markup = types.InlineKeyboardMarkup()
    btn4 = types.InlineKeyboardButton('YouTube kanal📺', url="https://www.youtube.com/@Madomoa_Brand")
    markup.add(btn4)
    bot.send_message(message.chat.id, 'YouTube kanalga o\'tish uchun pastdagi 👇 tugmani bosing !', reply_markup=markup)

##------------------------------------------------------------------------------------------------------------------------------------------
@bot.message_handler(func=lambda message: message.text == 'Admin bilan bog\'lanish👤')
def admin(message):
    markup = types.InlineKeyboardMarkup()
    btn3 = types.InlineKeyboardButton('Admin bilan bog\'lanish👤', url="https://t.me/madomoabrand")
    markup.add(btn3)
    bot.send_message(message.chat.id, 'Admin bilan bog\'lanish uchun pastdagi 👇 tugmani bosing !', reply_markup=markup)
##-------------------------------------------------------------------------------------------------------------------------------------------
@bot.message_handler(func=lambda message: message.text == '')

bot.polling()
