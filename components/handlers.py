import telebot
from components.menu import create_menu
from components.data import get_data 
from components.model import get_response, extract_output
from components.prompt import get_prompt

def register_handlers(bot):
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(message.chat.id, "Выберите валютную пару:", reply_markup=create_menu())

    @bot.message_handler(func=lambda message: True)
    def handle_currency_pair(message):
        symbol = message.text.strip()
        
        # Отправляем действие "печатает"
        bot.send_chat_action(message.chat.id, 'typing')
        
        # Получаем данные и обрабатываем запрос
        data = get_data(symbol)
        prompt_text = get_prompt(data)
        response = get_response(prompt_text)
        extracted_response = extract_output(response)
        
        # Отправляем ответ пользователю
        bot.send_message(message.chat.id, extracted_response)