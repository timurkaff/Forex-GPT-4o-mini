import telebot
import os
from dotenv import load_dotenv
from telebot import types
from components.data import get_data 
from components.model import get_response, extract_output
from components.prompt import get_prompt
from components.handlers import register_handlers
from components.config import TOKEN

bot = telebot.TeleBot(TOKEN)

if __name__ == "__main__":
    register_handlers(bot)
    bot.polling(none_stop=True)