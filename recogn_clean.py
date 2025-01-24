import easyocr
import cv2
import numpy as np
from getting_image.py import image_path

# Создаем объект Reader для русского и английского языков
reader = easyocr.Reader(["ru", "en"])

# Загружаем изображение
image = cv2.imread(image_path)

# Читаем текст из изображения и получаем детали (текст и координаты)
results = reader.readtext(image_path, detail=1)

# Список для хранения распознанных слов
recognized_words = []

# Проходим по результатам и перекрашиваем области текста в белый цвет
for (bbox, text, prob) in results:
    # Добавляем распознанный текст в список
    recognized_words.append(text)
    
    # Преобразуем координаты в целые числа
    points = np.array(bbox, dtype=np.int32)
    
    # Создаем маску для области текста
    cv2.fillPoly(image, [points], (255, 255, 255))  # Закрашиваем область текста белым цветом

# Сохраняем новое изображение с измененными цветами
output_image_path = 'output_image.jpg'
cv2.imwrite(output_image_path, image)


# Объединяем распознанные слова в одну строку
combined_text = ' '.join(recognized_words)
