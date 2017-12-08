import multiprocessing

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


@bot.message_handler(content_types=["text"])
def arithmetic(message):
    pool=Pool(processes=1)
    print(message.text)
    result=pool.apply_async(brain.Big_father, (str(message.text),))
    try:
        eval(str(result.get(timeout=1)))
    except multiprocessing.context.TimeoutError:
        crash=open('crash.mp3','rb')
        bot.send_voice(message.chat.id,crash)


if __name__ == '__main__':
    bot.polling(none_stop=True)
