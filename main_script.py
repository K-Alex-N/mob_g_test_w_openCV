import time

import imagehash
from PIL import Image


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
