import time

import cv2

#
#  БЫСТРЕ ПОЛУЧИТЬ РАЗМЕРЫ ИЗ PIL
#

def get_image_resolution(image_path):
    """
    Функция для определения разрешения изображения.

    Args:
      image_path: Путь к изображению.

    Returns:
      Кортеж (ширина, высота) изображения.
    """

    img = cv2.imread(image_path)
    height, width, channels = img.shape
    return width, height


# Пример использования
image_path = 'my_images/Screenshot2.jpg'
start = time.time()
width, height = get_image_resolution(image_path)
print(time.time() - start)
print(f"Ширина изображения: {width} пикселей")
print(f"Высота изображения: {height} пикселей")


from PIL import Image
start = time.time()
img = Image.open(image_path)
width, height = img.size
print(time.time() - start)