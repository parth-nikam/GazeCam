# virtual_keyboard.py

import cv2
import numpy as np


def create_keyboard(keys_set):
    keyboard = np.zeros((600, 1000, 3), np.uint8)
    width, height = 200, 200
    thickness = 3

    font_letter = cv2.FONT_HERSHEY_PLAIN
    font_scale = 10
    font_thickness = 4

    for i, key_text in keys_set.items():
        row, col = divmod(i, 5)
        x, y = col * width, row * height

        is_light = i == 5
        color = (255, 255, 255) if is_light else (255, 0, 0)

        cv2.rectangle(keyboard, (x + thickness, y + thickness), (x + width - thickness, y + height - thickness), color, -1)

        text_size = cv2.getTextSize(key_text, font_letter, font_scale, font_thickness)[0]
        text_x = int((width - text_size[0]) / 2) + x
        text_y = int((height + text_size[1]) / 2) + y

        cv2.putText(keyboard, key_text, (text_x, text_y), font_letter, font_scale, (255, 0, 0), font_thickness)

    return keyboard
