import config
import telebot
import brain

# from telebot import types

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
#    bot.register_next_step_handler(, hard_mode)



@bot.message_handler(content_types=["text"])
def arithmetic(message):

    #bot.send_message(message.chat.id,
    #                 simple_arithmetic.Arithmetic((message.text)).simple_arithmetic())
    eval(brain.Big_father(message.text).grafic())


if __name__ == '__main__':
    bot.polling(none_stop=True)
