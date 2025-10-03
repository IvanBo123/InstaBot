import telebot
from telebot import types
from instaparse import InstaParse as IP

# 🔑 Вставь сюда токен, который дал @BotFather
API_TOKEN = "8488922008:AAEhAxpTh4A2zqC7854pcXio-AXHP30CXpM"

bot = telebot.TeleBot(API_TOKEN)

# Обработка команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Привет! Я бот, с помощью которого ты можешь посмотреть фото и видео Instagram. Загрузи сюда ссылку поста и получи видео")

# Обработка любого текста
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    # markup = types.InlineKeyboardMarkup()
    # markup.add(
    #     types.InlineKeyboardButton("🔗 Получить медиа", url=IP(message.text).getURL())
    # )
    # , reply_markup=markup
    bot.reply_to(message, f"Ваша ссылка: {message.text}")
    response = IP(message.text).getURL()
    if response['status'] == 'error':
        bot.reply_to(message, f"{response['message']}")
    if response['status'] == 'success':
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton("🔗 Получить медиа", url=response['message'])
        )
        bot.reply_to(message, f"Ваша ссылка успешно обработана", reply_markup=markup)

# Запуск бота (будет работать, пока не остановишь скрипт)
bot.polling(none_stop=True)
