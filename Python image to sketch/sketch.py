import cv2

img = cv2.imread('2022-04-19_16.41.51.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
inverted = 255 - gray_img
blur = cv2.GaussianBlur(inverted, (21, 21), 0)
inverted_blur = 255 - blur
pencil = cv2.divide(gray_img, inverted_blur, scale=256.0)
cv2.imshow('orignal image', img)
cv2.imshow('sketch image', pencil)

cv2.waitKey(0)