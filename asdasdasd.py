import cv2 as cv
img = cv.imread(r"C:\Temp\res.png")

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("my_images/starry_night2.png", img)
