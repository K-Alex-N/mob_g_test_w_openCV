import cv2
import numpy as np

def find_template(image_path, template_path):

    img = cv2.imread(image_path, 0)  # Загружаем изображение в оттенках серого
    template = cv2.imread(template_path, 0)  # Загружаем шаблон в оттенках серого

    # Нормализация изображений
    img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
    template = cv2.normalize(template, None, 0, 255, cv2.NORM_MINMAX)

    w, h = template.shape[::-1]

    # Метод сопоставления шаблонов
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

    # Поиск локального максимума
    threshold = 0.8  # Порог сходства
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

    cv2.imshow('Detected', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if len(loc[0]) > 0:
        return loc[0][0], loc[1][0]
    else:
        return None

# Пример использования
image_path = 'starry_night.png'
template_path = 'target2.png'
result = find_template(image_path, template_path)

if result:
    print(f"Шаблон найден в координатах: {result}")
else:
    print("Шаблон не найден")