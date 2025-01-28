import cv2
from place_for_text import rect_image, top_left, bottom_right
from stroke import line
from recogn_clean import image
from PIL import Image, ImageDraw, ImageFont
import numpy as np

image_for_text = image.copy()

image_pil = Image.fromarray(cv2.cvtColor(image_for_text, cv2.COLOR_BGR2RGB))

rect_width = bottom_right[0] - top_left[0]
rect_height = bottom_right[1] - top_left[1]

new_text = line  

font_path = r"C:\Users\12\Documents\ivr\ffont.ttf"
font_size = rect_width // 9
font = ImageFont.truetype(font_path, font_size)

draw = ImageDraw.Draw(image_pil)

lines = new_text.split('\n')

current_y = top_left[1] + (rect_height - len(lines) * font_size) // 2

for line in lines:
    text_bbox = draw.textbbox((0, 0), line, font=font)
    text_width = text_bbox[2] - text_bbox[0]

    text_x = top_left[0] + (rect_width - text_width) // 2

    draw.text((text_x, current_y), line, font=font, fill=(0, 0, 0))  # Черный цвет текста

    current_y += font_size

image_with_text = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)

result_path = 'result.jpg'

cv2.imwrite(result_path, image_with_text)
