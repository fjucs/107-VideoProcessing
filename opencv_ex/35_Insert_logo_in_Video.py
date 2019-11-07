import cv2
import numpy as np
cap=cv2.VideoCapture(0)

img=cv2.imread('frame.png')
img=cv2.resize(img,(640,480))

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

ll = cv2.imread('ll.png')
ll = cv2.resize(ll, (200, 200))
ll_r = cv2.flip(ll, 1)

def putImg(img, icon, pos, thre):
    x, y = pos

    rows, cols, channels = icon.shape
    bg = img[y:rows+y, x:cols+x]

    img2gray = cv2.cvtColor(icon,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, thre, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    img_bg = cv2.bitwise_and(bg, bg, mask=mask_inv)
    img_fg = cv2.bitwise_and(icon, icon, mask=mask)

    cv2.imshow('img_bg', img_bg)
    cv2.imshow('img_fg', img_fg)

    dst = cv2.add(img_bg, img_fg)
    img[y:rows+y, x:cols+x] = dst
    return img

while(True):
    ret, frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    frame=cv2.flip(frame,1)

    dst = putImg(frame, img, (0, 0), 100)
    dst = putImg(dst, ll, (440, 280), 80)


    dst = putImg(dst, ll_r, (100, 280), 80)

    # print(dst)
    cv2.imshow('dst', dst)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()