
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

reader = easyocr.Reader(["ru", "en"])

image = cv2.imread(image_path)
print(image_path)

print(1)
results = reader.readtext(image_path, detail=1)
print(2)
recognized_words = []

for (bbox, text, prob) in results:
    recognized_words.append(text)
    
    points = np.array(bbox, dtype=np.int32)
    
    cv2.fillPoly(image, [points], (255, 255, 255))  # Закрашиваем область текста белым цветом

output_image_path = 'output_image.jpg'
cv2.imwrite(output_image_path, image)

print(3)
combined_text = ' '.join(recognized_words)

first_bbox = results[0][0]
first_coordinates = (int(first_bbox[0][0]), int(first_bbox[0][1]))
