import telebot
from telebot import types

bot = telebot.TeleBot('7543169821:AAH21rDta0DR6bxhddu6yVHi2C7BTnv7I-0')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Добро пожаловать в бота Кулиар!\nЗдесь вы найдете множество вкусных рецептов.")

    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Завтрак")
    btn2 = types.KeyboardButton("Обед")
    markup.row(btn1, btn2)
    btn3 = types.KeyboardButton("Ужин")
    btn4 = types.KeyboardButton("Десерт")
    markup.row(btn3, btn4)
    btn5 = types.KeyboardButton("Предложить рецепт")
    markup.row(btn5)

    bot.send_message(message.chat.id, "Выберите интересующую вас категорию:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Завтрак":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Омлет с овощами и сосисками', url='https://t.me/Top_kul1nar/3'))
        markup.add(types.InlineKeyboardButton('Хлопья', url='https://t.me/+_hLsm8pdiBs1MzBi'))
        markup.add(types.InlineKeyboardButton('Каша', url='https://t.me/+_hLsm8pdiBs1MzBi'))





        bot.send_message(message.chat.id, "Все рецепты:", reply_markup=markup)
    if message.text == "Обед":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Суп', url='https://t.me/+_hLsm8pdiBs1MzBi'))





        bot.send_message(message.chat.id, "Все рецепты:", reply_markup=markup)

    if message.text == "Ужин":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Картошка', url='https://t.me/+_hLsm8pdiBs1MzBi'))






        bot.send_message(message.chat.id, "Все рецепты:", reply_markup=markup)

    if message.text == "Десерт":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Торт', url='https://t.me/+_hLsm8pdiBs1MzBi'))






        bot.send_message(message.chat.id, "Все рецепты:", reply_markup=markup)

    if message.text == "Предложить рецепт":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Предложить рецепт', url='https://t.me/For_Kulinar_Bot'))






        bot.send_message(message.chat.id, "Предложить рецепт ТУТ:", reply_markup=markup)


if __name__ == "__main__":
    bot.polling(none_stop=True)
