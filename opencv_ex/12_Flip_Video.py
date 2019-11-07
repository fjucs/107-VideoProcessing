import numpy as np
import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Flip
    frame=cv2.flip(frame,1)

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print(type(gray))

    # Display the resulting frame
    cv2.imshow('frame',gray)
    cv2.imshow('frame2',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()