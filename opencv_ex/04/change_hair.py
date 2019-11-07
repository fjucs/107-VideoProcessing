# Change blue color to yellow color
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
yellow = np.full(frame.shape, (0, 255,255), dtype=np.uint8)
    
TH=100

# define range of the referenced color in RGB
lower_black = np.array([0, 0, 0])
upper_black = np.array([TH, TH, TH])

while(1):

    # Take each frame
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    mask = cv2.inRange(frame, lower_black, upper_black)

    # apply a series of erosions and dilations to the mask
    # using an elliptical kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    mask = cv2.erode(mask, kernel, iterations = 2)
    mask = cv2.dilate(mask, kernel, iterations = 2)
    mask_inv = cv2.bitwise_not(mask)
    # Bitwise-AND mask and original image
    fg = cv2.bitwise_and(yellow,yellow, mask= mask)
    bg = cv2.bitwise_and(frame, frame, mask= mask_inv)
    final = cv2.add(fg, bg)
    cv2.imshow('frame',frame)
    cv2.imshow('final',final)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()