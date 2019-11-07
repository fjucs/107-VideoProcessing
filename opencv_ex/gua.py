# Change blue color to yellow color
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
rows, columns, channels = frame.shape
mask01 = np.zeros((rows, columns), np.uint8)
yellow = np.full(frame.shape, (0, 255, 0), dtype=np.uint8)
    
# define range of blue color in HSV
lower_blue = np.array([110, 50, 50], dtype=np.uint8)
upper_blue = np.array([150,255,255], dtype=np.uint8)

frame = cv2.flip(frame, 1)

print(rows, columns)

img = cv2.imread('ll4.png')
img = cv2.resize(img, (1280, 720))

img2 = cv2.imread('ll5.jpg')
img2 = cv2.resize(img2, (1280, 720))

while(1):

    # Take each frame
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    yellowedFrame= cv2.addWeighted(frame, 0.7, yellow, 0.3, 0)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # apply a series of erosions and dilations to the mask
    # using an elliptical kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    mask = cv2.erode(mask, kernel, iterations = 2)
    mask = cv2.dilate(mask, kernel, iterations = 2)
    mask01 = cv2.bitwise_or(mask01, mask) # 新的內容
    mask02 = cv2.bitwise_not(mask01)
    # Bitwise-AND mask and original image
    # fg = cv2.bitwise_and(frame,frame, mask= mask01)
    print(frame.shape, img.shape)
    fg = cv2.bitwise_and(img,img, mask=mask01)
    bg = cv2.bitwise_and(img2, img2, mask= mask02)
    final = cv2.add(fg, bg)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('mask01',mask01)
    cv2.imshow('yellowedFrame',img2)
    cv2.imshow('final',final)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()