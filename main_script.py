import time

import imagehash
from PIL import Image

from get_image_dimentions import get_image_resolution


def is_images_different(img1: str, img2: str):
    start = time.time()
    hash0 = imagehash.phash(Image.open(img1))
    hash1 = imagehash.phash(Image.open(img2))
    print(time.time() - start)

    diff = hash0 - hash1
    if diff >= 1:
        print(f"Изображения отличаются. Diff = {diff}")
        return False
    return True


img1 = "comparison/5353018101685414245.jpg"
img2 = "comparison/5353018101685414245 - small diff.jpg"

is_images_different(img1, img2)

# проверить что язык английский, если нет то скриншот и выставить английский язык

image_path = 'Screenshot2.jpg'
width, height = get_image_resolution(image_path)

class TestMenuLives:

    def test_menu_lives__comparison_with_template(self):
        # сравнение с эталоном - эот сразу же и проверка английского языка
        # все сопровождать аллюр степами
        pass

    def test_menu_lives__text_in_all_languages(self):
        # проверка на других языках - выйти. включить другой язык. зайти снова. порезать, распознать текст и сверить с эталоном


        pass


