import telebot
from telebot import types
import logging
import os


@bot.message_handler(commands=['start'])
def start(message):
        application = Application.builder().token(
        os.environ.get("TOKEN")
    ).build()
    
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
        markup.add(types.InlineKeyboardButton('Панкейки', url='https://t.me/Top_kul1nar/5'))
        markup.add(types.InlineKeyboardButton('Оладьи с колбасой и сыром', url='https://t.me/Top_kul1nar/7'))
        markup.add(types.InlineKeyboardButton('Сырные кексы с зелёным луком', url='https://t.me/Top_kul1nar/17'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))

        bot.send_message(message.chat.id, "Все рецепты:", reply_markup=markup)
        
    if message.text == "Обед":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Сосиски в тесте', url='https://t.me/Top_kul1nar/8'))
        markup.add(types.InlineKeyboardButton('Курица под соусом терияки', url='https://t.me/Top_kul1nar/9'))
        markup.add(types.InlineKeyboardButton('Суп-пюре из тыквы', url='https://t.me/Top_kul1nar/10'))
        markup.add(types.InlineKeyboardButton('Рыбные котлеты из консервы', url='https://t.me/Top_kul1nar/18'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))
        
        bot.send_message(message.chat.id, "Все рецепты:", reply_markup=markup)

    if message.text == "Ужин":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))

        bot.send_message(message.chat.id, "Все рецепты:", reply_markup=markup)

    if message.text == "Десерт":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Творожно-банановый десерт', url='https://t.me/Top_kul1nar/6'))
        markup.add(types.InlineKeyboardButton('Шоколадные маффины "Брауни"', url='https://t.me/Top_kul1nar/12'))
        markup.add(types.InlineKeyboardButton('"Рафаэлло"', url='https://t.me/Top_kul1nar/15'))
        markup.add(types.InlineKeyboardButton('Пончики на сгущёнке', url='https://t.me/Top_kul1nar/16'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))
        markup.add(types.InlineKeyboardButton('Запеканка из картофеля и мясного фарша', url='https://t.me/Top_kul1nar/19'))
        
        bot.send_message(message.chat.id, "Все рецепты:", reply_markup=markup)

    if message.text == "Предложить рецепт":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Предложить рецепт', url='https://t.me/For_Kulinar_Bot'))

        bot.send_message(message.chat.id, "Предложить рецепт ТУТ:", reply_markup=markup)

if __name__ == "__main__":
    bot.polling(none_stop=True)
