import numpy as np
import cv2

def nothing(x):
	pass

cap = cv2.VideoCapture(1)

cv2.namedWindow('wind')
cv2.createTrackbar('t1', 'wind', 100, 255, nothing)

cv2.namedWindow('Edge')
cv2.createTrackbar('a', 'Edge', 100, 255, nothing)
cv2.createTrackbar('b', 'Edge', 200, 255, nothing)


while True:
	ret, frame = cap.read()

	frame = cv2.resize(frame, (500, 400))

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	ret, th = cv2.threshold(gray,cv2.getTrackbarPos('t1', 'wind') ,255,cv2.THRESH_BINARY)

	a = cv2.getTrackbarPos('a', 'Edge')
	b = cv2.getTrackbarPos('b', 'Edge')
	edge = cv2.Canny(gray, a, b)

	cv2.imshow('color', frame)
	cv2.imshow('gray', gray)
	cv2.imshow('wind', th)
	cv2.imshow('Edge', edge)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


cap.release()
cv2.destroyAllWindows()