import cv2
import numpy as np

def putImg(img, icon, pos, thre):
    x, y = pos

    rows, cols, channels = icon.shape
    bg = img[y:rows+y, x:cols+x]

    img2gray = cv2.cvtColor(icon, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, thre, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    img_bg = cv2.bitwise_and(bg, bg, mask=mask_inv)
    img_fg = cv2.bitwise_and(icon, icon, mask=mask)

    # cv2.imshow('img_bg', img_bg)
    # cv2.imshow('img_fg', img_fg)

    dst = cv2.add(img_bg, img_fg)
    img[y:rows+y, x:cols+x] = dst
    return img

def flip(frame, state):
    # x, y, both
    # 0, 1, -1
	return cv2.flip(frame, state)

def toGray(frame):
	return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def two_val(frame, thres=30):
    frame = toGray(frame)
    ret, tw = cv2.threshold(frame, thres, 255, cv2.THRESH_BINARY)
    return tw

def imshow(name, scr):
	cv2.imshow(name, scr)

def readImg(path):
	return cv2.imread(path)

def resize(img, w, h):
	return cv2.resize(img, (w, h), interpolation=cv2.INTER_CUBIC)

def threshold(frame, a):
	#two return value
	return cv2.threshold(frame, a, 255, cv2.THRESH_BINARY)

def Canny(frame, th1, th2):
	return cv2.Canny(frame, th1, th2)

#31_Splitting_and_Merging_Image.py
def splitBGR(frame):
	return cv2.split(frame)

def mergeColor(b, g, r):
	return cv2.merge((b, g, r))

def set0(frame):
	return np.zeros(frame.shape, np.uint8)