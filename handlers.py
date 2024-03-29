from aiogram import Router, types, Dispatcher, Bot
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F
from pymongo import MongoClient
from aiogram.enums.parse_mode import ParseMode

import kb
import text

router = Router()



conn = MongoClient("mongodb://localhost:27017/")
db = conn["tbot"]
collection = db["user_register"]

# bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()
# dp = Dispatcher(bot)


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")

async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)    



   
# @router.message(Command("start"))

# async def start_message(message: types.Message):
#     await message.answer("Здравствуйте! Вас приветствует бот магазина Nura.Kargo")

#     user_id = message.from_user.id
#     text = message.text
    
#     existing_user = collection.find_one({"user_id": user_id})
#     if existing_user:
#         await message.reply("Вы уже зарегистрированы")
#     else:  
         
#         await message.answer("Чтобы зарегистрироваться, отправьте свое имя, адрес и номер телефона в формате:\n\nИмя Фамилия\nАдрес\nНомер телефона")
        
#         if '\n' in text:
#             name, address, phone_number = text.split('\n', 2)
        
               
#         # Сохранение данных в MongoDB
#             user_data = {
#                 "user_id": user_id,
#                 "name": name,
#                 "address": address,
#                 "phone_number": phone_number
#             }
#             collection.insert_one(user_data)
        
#             await message.reply(f'Спасибо, {name}! Вы успешно зарегистрированы.\n\nВаш адрес: {address}\nВаш номер телефона: {phone_number}')
#         else:
#             await message.reply("Пожалуйста, отправьте свое имя, адрес и номер телефона в правильном формате.")
    

# @router.message(F.text.lower() == 'подробнее о нашем магазине')
# async def about(message: types.Message):
#     profile_url = "Это наш магазин [Nura.Kargo](https://www.instagram.com/nura.kargo?igsh=OTR5M2I4enpsZHY4&utm_source=qr)"
#     await message.reply(profile_url, parse_mode='Markdown')


# @router.message(Command("about"))    

# async def start(message: types.Message):
#     profile_url = "Это наш магазин [Nura.Kargo](https://www.instagram.com/nura.kargo?igsh=OTR5M2I4enpsZHY4&utm_source=qr)"
#     keyboard = types.InlineKeyboardMarkup()
#     keyboard.add(types.InlineKeyboardButton(text="Перейти в магазин", url="https://www.instagram.com/nura.kargo?igsh=OTR5M2I4enpsZHY4&utm_source=qr"))
#     await message.reply(profile_url, parse_mode='Markdown', reply_markup=keyboard)    
    
  
@dp.message(Command("hello"))
async def cmd_hello(message: Message):
    await message.answer(
        f"Hello, <b>{message.from_user.full_name}</b>",
        parse_mode=ParseMode.HTML
    )  
# @dp.message(Command("statistic"))  
# async def get_users_stat(message: types.Message):
#     unique_users = collection.distinct("user_id")
#     await message.reply("Статистика пользователей: " + ", ".join(map(str, unique_users)))
