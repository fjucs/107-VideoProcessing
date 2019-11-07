import numpy as np
import cv2

img = cv2.imread('fruits.jpg')
cv2.imshow('Original', img)

print(len(img))
print(len(img[0]))

cv2.waitKey(0)
cv2.destroyAllWindows()