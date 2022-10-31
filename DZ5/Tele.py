import telebot
from parsing import film_torr

# MyFirstDimawqwqwqwqwqwBot
bot = telebot.TeleBot('5642416642:AAH0H5GLtq_S7kihiyXxmn8Ref-hapj0yvA')

helper = 'Список команд\n' \
         'ft = FilmTorrent\n' \
         'op = Орел/Пешка\n'



@bot.message_handler(commands=['start'])
def start(message):
    mass = f'Привет {message.from_user.first_name}'
    bot.send_message(message.chat.id, mass, parse_mode='html')


@bot.message_handler(commands=['help'])
def start(message):
    # for k, v in helper.items():
    bot.send_message(message.chat.id, helper, parse_mode='html')



@bot.message_handler()
def get_user_text(message):
    if message.text.lower() == 'ft':
        films = film_torr()
        for i in films:
            bot.send_photo(message.chat.id, i[3])
            bot.send_message(message.chat.id, f"Название: {i[1]}\nРейтинг: {i[2]}\nСсылка: {i[0]}")

    elif message.text.lower() == 'op':
        import random
        img = {'орел': 'image/eagle.png', 'пешка': 'image/pawn.jpg'}
        choic_r = open(img.get(random.choice(list(img.keys()))),'rb')
        bot.send_message(message.chat.id, 'Игра Орел/Пешка')
        bot.send_photo(message.chat.id, choic_r)


    elif message.text.lower() == 'in':
        bot.send_message(message.chat.id, message, parse_mode='html')
    else:
        bot.send_message(message.chat.id, 'Не чего не понял! Напишете /help  что бы узнать команды.')


bot.polling(none_stop=True)
