import telebot
import os
import random
import wand

from telebot import types

TOKEN = '657360782:AAFwpCG8wWScmvvZHQx0QvuCt26SfmlMxaU'

bot = telebot.TeleBot(TOKEN)

user = bot.get_me()

def distort(fname):
    boi = "convert "+fname+" -liquid-rescale 400x400 result/"+fname
    os.system(boi)


@bot.message_handler(commands=['start'])
def send_welcome(msg):
    markup = types.InlineKeyboardMarkup()
    start_bt = types.InlineKeyboardButton('Contact', url="http://telegram.me/xtimms")
    markup.add(start_bt)
    bot.reply_to(msg, u"Welcome, {}. Just send your photo.".format(msg.from_user.first_name), reply_markup=markup)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Send me an image to distort it! Your photos are deleted after the distortion is complete! To prevent server from hitting its limit, the photo is downscaled to 320x320")


@bot.message_handler(content_types=['photo'])
def photudl(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    download = bot.download_file(file_info.file_path)
    file_name = str(random.randint(1,101))+".jpg"
    with open(file_name, 'wb') as new_file:
        new_file.write(download)
    distort(file_name)
    photo = open('result/'+file_name, 'rb')
    bot.send_photo(message.chat.id, photo)    

bot.polling()    
                                                
