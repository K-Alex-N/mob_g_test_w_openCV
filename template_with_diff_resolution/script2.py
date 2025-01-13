import cv2
import numpy as np

def find_template_in_image(image_path, template_path, threshold=0.8):
    """
    Функция для поиска шаблона в изображении с учетом масштабирования.

    Args:
        image_path: Путь к исходному изображению.
        template_path: Путь к шаблону.
        threshold: Порог соответствия (0.0 - 1.0).

    Returns:
        Кортеж с координатами верхней левой точки найденного шаблона или None, если шаблон не найден.
    """

    # Загрузка изображений в оттенках серого
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

    # Создание пирамиды изображений для поиска в разных масштабах
    w, h = template.shape[::-1]
    methods = [cv2.TM_CCOEFF_NORMED]  # Вы можете использовать другие методы сопоставления

    for mt in methods:
        img_copy = img.copy()

        # Сопоставление шаблона
        res = cv2.matchTemplate(img_copy, template, mt)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if max_val > threshold:
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            cv2.rectangle(img_copy, top_left, bottom_right, 255, 2)
            cv2.imshow('Detected Point', img_copy)
            cv2.waitKey(0)
            return top_left

    return None

# Пример использования
image_path = 'img.png'
template_path = 'target.png'
result = find_template_in_image(image_path, template_path)

if result:
    print(f"Шаблон найден в координатах: {result}")
else:
    print("Шаблон не найден")