import cv2
import numpy as np

# Загрузка изображений
image1 = cv2.imread('11.JPG')
image2 = cv2.imread('12.JPG')

# Создание маски для исключения областей
mask = np.zeros(image1.shape[:2], dtype="uint8")
cv2.rectangle(mask, (50, 50), (1200, 1200), 255, -1)  # Пример области для исключения

# Применение маски к изображениям
masked_image1 = cv2.bitwise_and(image1, image1, mask=mask)
masked_image2 = cv2.bitwise_and(image2, image2, mask=mask)

# Вычисление разницы между изображениями
difference = cv2.absdiff(masked_image1, masked_image2)

# Преобразование разницы в черно-белое изображение
grayscale = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)

# Применение порогового значения для выделения изменений
_, threshold = cv2.threshold(grayscale, 30, 255, cv2.THRESH_BINARY)

# Отображение результирующего изображения
cv2.imshow('Разница между изображениями', threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()