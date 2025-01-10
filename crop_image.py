import time

#
# OpenCV в большинстве случаев РАБОТАЕТ БЫСТРЕЕ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# быстрее для png но медленее для jpg
#


import cv2

for row_img in ('123.png', '5353018101685414307.jpg', 'starry_night2.png'):
    
    def crop_image(img, x, y, w, h):
        """
        Обрезает изображение.

        Args:
            img: Исходное изображение.
            x: Координата x левого верхнего угла области обрезки.
            y: Координата y левого верхнего угла области обрезки.
            w: Ширина области обрезки.
            h: Высота области обрезки.

        Returns:
            Обрезанное изображение.
        """

        crop_img = img[y:y+h, x:x+w]
        return crop_img

    start_time = time.time()
    img = cv2.imread(row_img)
    cropped_img = crop_image(img, 100, 50, 200, 150)  # Обрезаем область со стартовыми координатами (100, 50) и размером 200x150 пикселей
    cv2.imwrite('1.png', cropped_img)
    print(time.time() - start_time)


    # # Отображение результата
    # cv2.imshow("Cropped Image", cropped_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # _____________________________________________________________________

    from PIL import Image

    def crop_image(img, box):
        """
        Обрезает изображение.

        Args:
            img: Исходное изображение.
            box: Кортеж (left, upper, right, lower), определяющий область обрезки.

        Returns:
            Обрезанное изображение.
        """

        cropped_img = img.crop(box)
        return cropped_img

    start_time = time.time()
    img = Image.open(row_img)
    cropped_img = crop_image(img, (100, 50, 300, 200))  # Область обрезки: левая, верхняя, правая, нижняя координаты
    cropped_img.save('2.png')
    print(time.time() - start_time)