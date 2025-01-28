from googletrans import Translator
from recogn_clean import combined_text

translator = Translator()
translated_text = translator.translate(combined_text, src='en', dest='ru').text

translated_text_upper = translated_text.upper()
translated_words_list = translated_text_upper.split()
