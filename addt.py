import cv2
from place_for_text import rect_image, top_left, bottom_right
from stroke import line
from recogn_clean import image
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Загрузка изображения
image_for_text = image.copy()

# Преобразуем изображение в формат PIL
image_pil = Image.fromarray(cv2.cvtColor(image_for_text, cv2.COLOR_BGR2RGB))

# Вычисляем размеры прямоугольника
rect_width = bottom_right[0] - top_left[0]
rect_height = bottom_right[1] - top_left[1]

# Текст для добавления
new_text = line  

# Устанавливаем шрифт и параметры текста
font_path = r"C:\Users\12\Documents\ivr\ffont.ttf"
font_size = rect_width // 9
font = ImageFont.truetype(font_path, font_size)

# Создаем объект для рисования
draw = ImageDraw.Draw(image_pil)

# Разбиваем текст на строки (например, по символу новой строки)
lines = new_text.split('\n')

# Начальная y-координата для первой строки
current_y = top_left[1] + (rect_height - len(lines) * font_size) // 2

# Накладываем каждую строку текста на изображение
for line in lines:
    # Получаем размеры текущей строки с использованием textbbox()
    text_bbox = draw.textbbox((0, 0), line, font=font)
    text_width = text_bbox[2] - text_bbox[0]

    # Вычисляем координаты для центрирования текущей строки внутри прямоугольника
    text_x = top_left[0] + (rect_width - text_width) // 2

    # Накладываем текст на изображение
    draw.text((text_x, current_y), line, font=font, fill=(0, 0, 0))  # Черный цвет текста

    # Обновляем y-координату для следующей строки
    current_y += font_size

# Преобразуем обратно в формат OpenCV
image_with_text = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)

result_path = 'result.jpg'

# Сохраняем измененное изображение
cv2.imwrite(result_path, image_with_text)

print(bottom_right[0]-top_left[0])

# # Отображаем изображение (опционально)
# cv2.imshow("Image with Text", image_with_text)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
