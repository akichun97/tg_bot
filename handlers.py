from aiogram import Router, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F

router = Router()


@router.message(Command("start"))
async def start_handler(message: types.Message):
    kb = [
        [types.KeyboardButton(text = 'Сделать заказ')],
        [types.KeyboardButton(text = 'Подробнее о нашем магазине')]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите пожалуйста ниже"
        )
    await message.answer("Здравствуйте! Вас приветствует бот магазина Nura.Kargo", reply_markup=keyboard)
    
    
    
@router.message(F.text.lower() == 'сделать заказ')
async def order(message: types.Message):
    await message.reply("Для оформления заказа выберите команду /order")


@router.message(F.text.lower() == 'подробнее о нашем магазине')
async def about(message: types.Message):
    profile_url = "Это наш магазин [Nura.Kargo](https://www.instagram.com/nura.kargo?igsh=OTR5M2I4enpsZHY4&utm_source=qr)"
    await message.reply(profile_url, parse_mode='Markdown')
    
    

   
    
