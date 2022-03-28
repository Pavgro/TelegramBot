import telebot
from telebot import types

bot = telebot.TeleBot('Your API Token')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Web Development')
    btn2 = types.KeyboardButton('Games Development')
    btn3 = types.KeyboardButton('Mobile Development')
    btn4 = types.KeyboardButton('Machine Learning')
    markup.add(btn1, btn2, btn3,  btn4)
    send_message = f"<b>Hi {message.from_user.first_name} {message.from_user.last_name}</b>!\n" \
                   f"What field interests you?"

    bot.send_message(message.chat.id, send_message,parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def choose_interest_field(message):
    good_choice_message = "Good choice, open the site and start learning now\n Good Luck!"
    get_message = message.text.strip().lower()
    if get_message == "games development":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Unity")
        btn2 = types.KeyboardButton("Unreal Engine")
        markup.add(btn1,btn2)
        bot.send_message(message.chat.id,
                         "You need to choose the engine you want to develop with ", parse_mode='html', reply_markup=markup)

    elif get_message == "unity":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Unity course", url="https://www.udemy.com/course/unitycourse/"))
        bot.send_message(message.chat.id, good_choice_message, parse_mode='html', reply_markup=markup)

    elif get_message == "unreal engine":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Unreal engine course", url="https://www.udemy.com/course/unrealcourse/"))
        bot.send_message(message.chat.id, good_choice_message, parse_mode='html', reply_markup=markup)

    elif get_message == "mobile development":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("iOS")
        btn2 = types.KeyboardButton("Android")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id,
                         "You need to choose the operating system you want to develop for it",
                         parse_mode='html', reply_markup=markup)

    elif get_message == "android":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Android course",
                                              url="https://www.udemy.com/course/android-kotlin-developer/"))
        bot.send_message(message.chat.id,  good_choice_message, parse_mode='html', reply_markup=markup)

    elif get_message == "ios":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("iOS course",
                                              url="https://www.udemy.com/course/ios-13-app-development-bootcamp/"))
        bot.send_message(message.chat.id, good_choice_message, parse_mode='html', reply_markup=markup)

    elif get_message == "web development":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Full stack course", url="https://www.udemy.com/course/the-web-developer-bootcamp/"))
        bot.send_message(message.chat.id, good_choice_message, parse_mode='html', reply_markup=markup)

    elif get_message == "machine learning":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Machine Learning course",
                                              url="https://www.udemy.com/course/machinelearning/"))
        bot.send_message(message.chat.id, good_choice_message, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)
