
import logging
logging.basicConfig(
    level=10,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

import easyocr
import cv2
import numpy as np
from getting_image import image_path

# Создаем объект Reader для русского и английского языков
reader = easyocr.Reader(["ru", "en"])

# Загружаем изображение
image = cv2.imread(image_path)
print(image_path)

print(1)
# Читаем текст из изображения и получаем детали (текст и координаты)
results = reader.readtext(image_path, detail=1)
print(2)
# Список для хранения распознанных слов
recognized_words = []

# Проходим по результатам и перекрашиваем области текста mв белый цвет
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

print(3)
# Объединяем распознанные слова в одну строку
combined_text = ' '.join(recognized_words)

first_bbox = results[0][0]
first_coordinates = (int(first_bbox[0][0]), int(first_bbox[0][1]))
# print(first_coordinates)
# cv2.imshow('hhg', image)
# cv2.waitKey(0)