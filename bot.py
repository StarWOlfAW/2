import telebot;
bot = telebot.TeleBot('7099171935:AAFzM9yMXxu84v4FpUrkwLYBYef3fIRjiF4')
first = 'Ключкответуы'
second = 'sыыы'
result = 0
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Введите первую цифру")
        bot.register_next_step_handler(message, get_first)
    else:
        bot.send_message(message.from_user.id, 'Напиши /start')

def get_first(message):
    global first
    while first == 'Ключкответуы':
        try:
            first = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Вводите цифры')
    bot.send_message(message.from_user.id, 'Введите вторую цифру')
    bot.register_next_step_handler(message, get_second)
def get_second(message):
    global second
    while second == 'sыыы':
        try:
            second = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Вводите цифры')
    second = int(message.text)
    result = int(first - second)
    bot.send_message(message.from_user.id, 'Ответ' + '  ' + str(int(result)))
    bot.register_next_step_handler(message, start)
bot.polling(none_stop=True, interval=0)

