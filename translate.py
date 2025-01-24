from googletrans import Translator
from recogn_clean.py import combined_text

# Переводим объединенный текст с английского на русский
translator = Translator()
translated_text = translator.translate(combined_text, src='en', dest='ru').text

# Приводим переведенный текст к верхнему регистру и разбиваем на список слов
translated_text_upper = translated_text.upper()
translated_words_list = translated_text_upper.split()