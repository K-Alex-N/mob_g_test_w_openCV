import cv2 as cv
img = cv.imread(r"C:\screen.png")

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("starry_night.png", img)
