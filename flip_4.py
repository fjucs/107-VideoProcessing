import numpy as np
import cv2

cap = cv2.VideoCapture(1)
ret, frame = cap.read()

def flip_x(img):
	return cv2.flip(img, 0)

def flip_y(img):
	return cv2.flip(img, 1)

def flip_both(img):
	return cv2.flip(img, -1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    frame = cv2.resize(frame, (500, 400))

    frame = cv2.flip(frame, 1)
    # Flip
    w0 = frame
    w1 = flip_y(frame)
    w2 = flip_x(frame)
    w3 = flip_both(frame)

    # Display the resulting frame
    cv2.imshow('1', w0)
    cv2.imshow('2', w1)
    cv2.imshow('3', w2)
    cv2.imshow('4', w3)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()