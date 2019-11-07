import cv2
import numpy as np

# Load two images
sample = cv2.imread('sample.jpg')
logo = cv2.imread('logo.png')
logo = cv2.resize(logo, (200, 200))
cv2.imshow('logo',logo)

y = 0
x = 160

print(sample.shape)

# 切背景
rows,cols,channels = logo.shape
bg = sample[y:rows+y, x:cols+x]

# 準備mask
img2gray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 50, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# 處理背景
p_bg = cv2.bitwise_and(bg, bg, mask=mask_inv)
# 處理前景
p_fg = cv2.bitwise_and(logo, logo, mask=mask)

# 合併
dst = cv2.add(p_bg, p_fg)

# 放回大圖
sample[y:rows+y, x:cols+x ] = dst

cv2.imshow('1', sample)

cv2.waitKey(0)
cv2.destroyAllWindows()
