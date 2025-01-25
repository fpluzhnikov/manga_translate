import cv2
import numpy as np
from recogn_clean import output_image_path, image, first_coordinates

thresh = 130
img = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)[1]

x = first_coordinates[0]
y = first_coordinates[1]

x1 = 0
y1 = 0
x2 = 0
y2 = 0



col = True
while col:
    pix = img[y, x]
    if (pix == [0, 0, 0]).all():
        #print(x, y)
        x1 = x
        y1 = y
        col = False
    else:
        x += 1

x -= 1

col = True
while col:
    pix = img[y, x]
    if (pix == [0, 0, 0]).all():
        #print(x, y)
        x2 = x
        y2 = y
        col = False
    else:
        x -= 1

x3 = 0
y3 = 0
x4 = 0
y4 = 0

x = (x1-x2)//2+x2

col = True
while col:
    pix = img[y, x]
    if (pix == [0, 0, 0]).all():
        #print(x, y)
        x3 = x
        y3 = y
        col = False
    else:
        y -= 1

y += 1
col = True
while col:
    pix = img[y, x]
    if (pix == [0, 0, 0]).all():
        #print(x, y)
        x4 = x
        y4 = y
        col = False
    else:
        y += 1

y = (y4-y3)//2+y3

n1 = x
n2 = y

col = True
while col:
    pix = img[y, x]
    if (pix == [0, 0, 0]).all():
        #print(x, y)
        x1 = x
        y1 = y
        col = False
    else:
        x += 1

x -= 1

col = True
while col:
    pix = img[y, x]
    if (pix == [0, 0, 0]).all():
        #print(x, y)
        x2 = x
        y2 = y
        col = False
    else:
        x -= 1

x01 = x2+((x1-x2)//16*3)
y01 = y3+((y4-y3)//16*3)

x02 = x1-((x1-x2)//16*3)
y02 = y4-((y4-y3)//16*3)

max_w = x02-x01
max_h = y02-y01

# Позиция и размер прямоугольника
rectangle_position = (x01, y01, x02, y02)
top_left = (rectangle_position[0], rectangle_position[1])
bottom_right = (rectangle_position[2], rectangle_position[3])
