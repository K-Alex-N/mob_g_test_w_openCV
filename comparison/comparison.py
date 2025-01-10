import cv2
import numpy as np

def find_differences(img1, img2):
    # Загружаем изображения
    img1 = cv2.imread(img1)
    img2 = cv2.imread(img2)

    # Преобразуем изображения в оттенки серого
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Вычисляем разницу между изображениями
    diff = cv2.absdiff(gray1, gray2)

    # Применяем пороговое значение для выделения различий
    thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)[1]

    # Визуализация различий
    cv2.imshow('Difference Image', thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Пример использования
img1_path = '5353018101685414245.jpg'
# img2_path = '5353018101685414245---2.jpg'
img2_path = '5353018101685414245 - Diff.jpg'
find_differences(img1_path, img2_path)