
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu = [
    [InlineKeyboardButton(text="Подробнее о нашем магазине", callback_data="about")],
    [InlineKeyboardButton(text="Регистрация", callback_data="registration")],
    [InlineKeyboardButton(text="Отслеживать товары", callback_data="search_prod")],
    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")],
    [InlineKeyboardButton(text="Оформить заказ", callback_data="order")]
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])



# menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
# menu_keyboard.add(types.KeyboardButton('/start'))
# menu_keyboard.add(types.KeyboardButton('/help'))
# menu_keyboard.add(types.KeyboardButton('/settings'))
# menu_keyboard.add(types.KeyboardButton('/about'))
# menu_keyboard.add(types.KeyboardButton('/order'))

