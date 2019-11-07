import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	frame = cv2.resize(frame, (500, 500))
	frame = cv2.flip(frame, 1)

	# Our operations on the frame come here
	b, g, r = cv2.split(frame)
	z= np.zeros(b.shape, np.uint8)

	# Display the resulting frame
	cv2.imshow('frame',frame)
	cv2.imshow('r',cv2.merge((z, z, r)))
	cv2.imshow('g',cv2.merge((z, g, z)))
	cv2.imshow('b',cv2.merge((b, z, z)))
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()