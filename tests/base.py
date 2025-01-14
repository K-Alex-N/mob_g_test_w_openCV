import os

import cv2

WORK_DIR = os.path.dirname(os.path.abspath(os.curdir))


def compare_images_with_mask(img1_path, img2_path, mask_path):
    """
    Сравнивает два изображения, исключая область, заданную маской.

    Args:
        img1_path: Путь к первому изображению.
        img2_path: Путь к второму изображению.
        mask_path: Путь к маске.

    Returns:
        Значение метрики сходства.
    """

    # Загрузка изображений и маски
    img1 = cv2.imread(img1_path, 0)
    img2 = cv2.imread(img2_path, 0)
    mask = cv2.imread(mask_path, 0)

    # Применение маски
    masked_img1 = cv2.bitwise_and(img1, img1, mask=mask)
    masked_img2 = cv2.bitwise_and(img2, img2, mask=mask)

    # difference = cv2.absdiff(masked_img1, masked_img2)
    # cv2.imshow('Разница между изображениями', difference)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Сравнение изображений (например, структурное сходство)
    ssim = cv2.matchTemplate(masked_img1, masked_img2, cv2.TM_SQDIFF_NORMED)

    return ssim
