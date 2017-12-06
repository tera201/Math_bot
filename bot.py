import config
import telebot
import brain
from multiprocessing import Pool

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'привет')
    pass


@bot.message_handler(commands=['?', 'help'])
def handle_start(message):
    bot.send_message(message.chat.id, config.help_txt)
    pass



@bot.message_handler(commands=['hard_mode'])
def log(message):
    bot.send_message(message.chat.id, 'Ублюдок, мать твою, а ну иди сюда!')



@bot.message_handler(content_types=["text"])
def arithmetic(message):
    pool=Pool(processes=4)
    print(message.text)
    result=pool.apply_async(brain.Big_father, (str(message.text),))
    try:
        eval(str(result.get(timeout=1)))
    except Exception:
        bot.send_message(message.chat.id, '(X_X)')


if __name__ == '__main__':
    bot.polling(none_stop=True)
