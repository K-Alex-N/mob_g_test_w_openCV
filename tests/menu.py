import os
import time

from tests.base import compare_images_with_mask, WORK_DIR


# запустить приложение
# ждать
# повторять 5 раз по 5 секунд
#     получить скриншот и затем проверить
#     если не совпало то сохранить скриншоты (было, получили, разница)
# нажать следующее меню


def test_main_menu_screenshot():
    # target
    img1_path = os.path.join(WORK_DIR, r'images\menu\main_menu\11.JPG')
    # take screenshot with ADB
    img2_path = os.path.join(WORK_DIR, r'images\menu\main_menu\12.JPG')
    mask_path = os.path.join(WORK_DIR, r'images\menu\main_menu\10 - mask.JPG')

    similarity = compare_images_with_mask(img1_path, img2_path, mask_path)
    print("Сходство изображений:", similarity)

    if similarity > 0.00001:
        print('"Pictures are different"')
        return False
        # raise "Pictures are different"
        # take screenshots
    return True


def click_on_menu_shop():
    ...
    # subfunction tap()
    # click with ADB in coord


def click_on_menu_lives():
    pass


def tap_on_menu_settings():
    pass


def exit_from_menu():
    pass


def compare_menu_shop_screenshot():
    pass
    # через разные меню зайти и сравнить скриншоты
    # click_on_menu_shop1()
    # click_on_menu_shop2()
    # compare_images_with_mask():


def compare_menu_lives_screenshot():
    pass
    # compare_images_with_mask():


def test_startup():
    # вынести в фикстуру или функцию startup
    time.sleep(5)
    for _ in range(5):
        if test_main_menu_screenshot():
            break

    # test_main_menu_screenshot()

class TestMenu:

    def test_menu_screenshots(self):

        click_on_menu_shop()
        compare_menu_shop_screenshot()
        exit_from_menu()

        click_on_menu_lives()
        compare_menu_lives_screenshot()
        exit_from_menu()

        tap_on_menu_settings()
        # menu levels



    def test_text_in_menu(self):
        pass
