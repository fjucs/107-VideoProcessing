import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while True:
	# Capture frame-by-frame
	ret, frame = cap.read()

	frame = cv2.resize(frame, (500, 500))
	frame = cv2.flip(frame, 1)

	rows, cols, ch = frame.shape

	bimg=frame.copy()
	for i in range(rows):
		for j in range(cols):
			bimg[i][j][1]=0
			bimg[i][j][2]=0
			
	gimg=frame.copy()
	for i in range(rows):
		for j in range(cols):
			gimg[i][j][0]=0
			gimg[i][j][2]=0
			
	rimg=frame.copy()
	for i in range(rows):
		for j in range(cols):
			rimg[i][j][0]=0
			rimg[i][j][1]=0

	cv2.imshow('frame',frame)
	cv2.imshow('r', rimg)
	cv2.imshow('g', gimg)
	cv2.imshow('b', bimg)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()