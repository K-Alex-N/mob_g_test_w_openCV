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
    # click with ADB in coord

def click_on_menu_lives():
    pass

def exit_from_menu():
    pass

def compare_menu_shop_screenshot():
    pass
    # compare_images_with_mask():

def compare_menu_lives_screenshot():
    pass
    # compare_images_with_mask():



if __name__ == "__main__":

    # вынести в фикстуру или функцию startup
    time.sleep(5)
    for _ in range(5):
        if test_main_menu_screenshot():
            break

    # test_main_menu_screenshot()




def test_menu_by_screenshots():


    click_on_menu_shop()
    compare_menu_shop_screenshot()
    exit_from_menu()

    click_on_menu_lives()
    compare_menu_lives_screenshot()
    exit_from_menu()
