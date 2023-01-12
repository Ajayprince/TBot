import sensitive_info
import telebot

BOT_TOKEN = sensitive_info.API_KEY

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, 'Hey Amigo!! Welcome, I am a Calculator Bot')

@bot.message_handler(func=lambda message:True)
def handle_messages(message):
    bot.reply_to(message, f'The result is {eval(message.text)}')

print('Bot is up and running...')

bot.infinity_polling()