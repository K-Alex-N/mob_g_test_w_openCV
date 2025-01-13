import cv2
import numpy as np

def find_template(img, template):
    # Преобразуем изображения в оттенки серого
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Метод сопоставления шаблонов
    res = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # Поиск максимального значения
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # Рисуем прямоугольник вокруг найденного шаблона
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img,top_left, bottom_right, 255, 2)

    cv2.imshow('Detected Point',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_path = 'img.png'
template_path = 'target.png'
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
find_template(img, template)
