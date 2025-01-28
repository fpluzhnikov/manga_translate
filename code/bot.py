import telebot
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os
from io import BytesIO
import telebot
import subprocess
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Отправь мне изображение, и я добавлю на него текст.")

@bot.message_handler(content_types=['photo'])
def handle_image(message):
    try:
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        image_path = 'input_image.jpg'
        with open(image_path, 'wb') as new_file:
            new_file.write(downloaded_file)

        subprocess.run(["python", "addt.py", image_path, "Пример текста", "arial.ttf", "output.jpg"])

        with open("result.jpg", "rb") as result_file:
            bot.send_photo(message.chat.id, result_file)
            print('Картинка переведена')

        os.remove(image_path)
        os.remove("result.jpg")
        os.remove("output_image.jpg")
        os.remove('rectangle_image_with_rectangle.jpg')

    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {e}")

# Запуск бота
bot.polling()
