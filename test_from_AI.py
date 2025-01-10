import cv2
import numpy as np

# Загружаем исходное изображение и шаблон
img = cv2.imread('my_images/starry_night.png', 0)  # Загружаем в оттенках серого
template = cv2.imread('my_images/target.png', 0)  # Шаблон, который будем искать

# Метод сопоставления шаблонов
w, h = template.shape[::-1]

# Все методы сопоставления:
# method = cv2.TM_CCOEFF
# method = cv2.TM_CCOEFF_NORMED
# method = cv2.TM_CCORR
# method = cv2.TM_CCORR_NORMED
# method = cv2.TM_SQDIFF
method = cv2.TM_SQDIFF_NORMED

# Выполняем сопоставление
res = cv2.matchTemplate(img,template,method)

# Нормализуем результаты
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# Для каждого метода сопоставления, разные значения
# означают разные результаты
if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    top_left = min_loc
else:
    top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

# Рисуем прямоугольник вокруг найденного шаблона
cv2.rectangle(img,top_left, bottom_right, 255, 2)

# Отображаем результат
cv2.imshow('Detected',img)
cv2.waitKey(0)
cv2.destroyAllWindows()