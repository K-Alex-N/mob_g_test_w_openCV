# pip install pytesseract  + добавить в PATH!!!!!!!!!!!!!!!!!!!!!!

import pytesseract
from PIL import Image

# Указываем путь к изображению и язык распознавания
img_path = 'comparison/5353018101685414245.jpg'
# lang = 'rus'  # Для русского языка
lang = 'eng'  #

# Загружаем изображение
img = Image.open(img_path)

# List of available languages
print(pytesseract.get_languages(config=''))

# Распознаем текст
# text = pytesseract.image_to_string(img, lang=lang)

# Выводим результат
# print(text)