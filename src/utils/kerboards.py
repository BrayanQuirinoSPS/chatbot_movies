from telebot import types

def get_main_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup.add(types.KeyboardButton('recomendacion'))
    markup.add(types.KeyboardButton('recommendation'))
    markup.add(types.KeyboardButton('Hide Keyboard'))
    return markup

#Borra el teclado
def get_clear_keyboard():
    return types.ReplyKeyboardRemove(selective=False)
