#  pip install ImageHash
# почитать - https://pythonhow.com/what/imagehash-library-tutorial/
import imagehash
from PIL import Image

img1 = Image.open('5353018101685414245.jpg')
img2 = Image.open('5353018101685414245 - very small diff.jpg')
# img2 = Image.open('5353018101685414245 - small diff.jpg')
# img2 = Image.open('5353018101685414245 - Diff.jpg')
# img2 = Image.open('5353018101685414245 - big diff.jpg')

# whash: Wavelet hash, useful for detecting scaled images. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! - протестить!!!

# hash0 = imagehash.average_hash(img1)
hash0 = imagehash.phash(img1)
hash1 = imagehash.phash(img2)
# hash1 = imagehash.average_hash(img2)


diff = hash0 - hash1
print(diff)
if diff >= 1:
    print("Изображения отличаются")