import telebot
import random

bot = telebot.TeleBot("################################")
candies = 117

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
        message, f"Количество конфет{candies}\nКакое количество конфет,от 1 до 28,вы возьмёте?")


@bot.message_handler(content_types=["text"])
def game(message):
    global candies
    player = int(message.text)
    while candies > 0:
        if player < 1 or player > 28:
            bot.reply_to(
                message, 'Количество конфет должно быть от 1 до 28 !!!')
            bot.register_next_step_handler(message, content_types=["text"])
        else:
            candies -= player
            if candies == 0:
                bot.reply_to(message, 'Вам сегодня везет !')
                candies = 117
                bot.register_next_step_handler(commands=['start', 'help'])
            elif candies > 0:
                x = candies % 29
                if x == 0:
                    x = random.randint(1, 28)
                    candies -= x
                    bot.reply_to(
                        message, f'Крупье забирает {x}\nКоличество конфет {candies}')
                    bot.register_next_step_handler(
                        message, content_types=["text"])
                else:
                    candies -= x
                    bot.reply_to(
                        message, f'Крупье забирает {x}\nКоличество конфет {candies}')
                    if candies == 0:
                        bot.reply_to(message, 'Казино опять в плюсе !')
                        candies = 117
                        bot.register_next_step_handler(
                            commands=['start', 'help'])
                    else:
                        bot.register_next_step_handler(
                            message, content_types=["text"])


bot.infinity_polling()
