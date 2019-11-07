import cv2
import numpy as np
from color_manip import *
from bar import *

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

t = TrackBar('1', 'b')
while 1:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    frame, _, _ = color_detect(frame, 'skin', t.getTrackbarPos())
    cv2.imshow('1', frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()