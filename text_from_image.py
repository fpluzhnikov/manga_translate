import easyocr
import cv2
from getting_image.py import image_path

# Создаем объект Reader для русского и английского языков
reader = easyocr.Reader(["ru", "en"])

# Загружаем изображение
image = cv2.imread(image_path)

# Читаем текст из изображения и получаем детали (текст и координаты)
results = reader.readtext(image_path, detail=1)

# Список для хранения распознанных слов
recognized_words = []