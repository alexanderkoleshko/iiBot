import telebot
import random

TOKEN = '1076129447:AAESJcevUf2zQiNXIcQ4Wpm8-fCOZ7dBthw'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_handler(message):
    if message.from_user.id == 385474362:
        bot.send_message(message.chat.id, 'Привет, Лерочка!\nЭто небольшой подарок на 14 февраля моему солнышку! Введи '
                                          '/all, чтобы увидеть все то, что может этот бот ❤️')
    if message.from_user.id == 175676243:
        bot.send_message(message.chat.id, 'Привет, хозяин!')
    else:
        bot.reply_to(message, 'Чао, персик!')
        return


@bot.message_handler(commands=['all'])
def all_commands(message):
    if message.from_user.id == 385474362 or message.from_user.id == 175676243:
        bot.send_message(message.chat.id, '/photo - увидишь одно милое совместное фото!\n/birthday - если забыла, когда'
                                          ' у твоего любимого день рождения!\n/choose - если не можете решить, кто сего'
                                          'дня выбирает фильм, да и вообше, что угодно решить!!\n/anniversary - напомн'
                                          'ю, когда годовщина, а то ты постоянно забываешь 🥺')
    else:
        bot.send_message(message.chat.id, 'Ну-ка брысь отсюда!')
        return


@bot.message_handler(commands=['birthday'])
def bd(message):
    if message.from_user.id == 385474362 or message.from_user.id == 175676243:
        bot.send_message(message.chat.id, 'День рождения твоего парня 24 мая! Лера, пора бы уже запомнить!')
    else:
        bot.send_message(message.chat.id, 'Аривидерчи!')
        return


@bot.message_handler(commands=['choose'])
def randomiser(message):
    if message.from_user.id == 385474362 or message.from_user.id == 175676243:
        who = random.randint(0, 1)
        if who == 0:
            who = 'Sasha'
        else:
            who = 'Lera'
        bot.send_message(message.chat.id, who)
    else:
        bot.send_message(message.chat.id, 'Покеда!')
        return


@bot.message_handler(commands=['anniversary'])
def anniversary_command(message):
    if message.from_user.id == 385474362 or message.from_user.id == 175676243:
        bot.send_message(message.chat.id, 'Лера, 18 мая, запомни! Каждое утро 18-ого числа поздравляй своего любимого '
                                          'с годовщиной! Не обижай его!!!')
    else:
        bot.send_message(message.chat.id, 'Чао-какао!')
        return


@bot.message_handler(commands=['photo'])
def random_photo(message):
    if message.from_user.id == 385474362 or message.from_user.id == 175676243:
        photo1 = 'https://ibb.co/M5Kn9Pk'
        photo2 = 'https://ibb.co/37VczrM'
        photo3 = 'https://ibb.co/T0Cq77t'
        photo4 = 'https://ibb.co/dkYMVST'
        photo5 = 'https://ibb.co/jgQjf0x'
        photo6 = 'https://ibb.co/hZ7WGXZ'
        photo7 = 'https://ibb.co/Prdj9M6'
        photo8 = 'https://ibb.co/7VLzycV'
        photo9 = 'https://ibb.co/7NrSJDF'
        photo10 = 'https://ibb.co/mSs67Mn'
        random_photos = random.randint(1, 10)
        if random_photos == 1:
            random_photos = photo1
        if random_photos == 2:
            random_photos = photo2
        if random_photos == 3:
            random_photos = photo3
        if random_photos == 4:
            random_photos = photo4
        if random_photos == 5:
            random_photos = photo5
        if random_photos == 6:
            random_photos = photo6
        if random_photos == 7:
            random_photos = photo7
        if random_photos == 8:
            random_photos = photo8
        if random_photos == 9:
            random_photos = photo9
        if random_photos == 10:
            random_photos = photo10
        bot.send_photo(message.chat.id, random_photos)
    else:
        bot.send_message(message.chat.id, 'Это не для тебя!')
        return


bot.polling(none_stop=True, interval=0)