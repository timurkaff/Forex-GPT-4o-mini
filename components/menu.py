from telebot import types

def create_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "EURUSD=X",
        "AUDUSD=X",
        "GBPUSD=X",
        "USDJPY=X"
    ]
    for button in buttons:
        markup.add(types.KeyboardButton(button))
    return markup
