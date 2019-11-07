import cv2
import numpy as np
import pygame

# face
cascPath = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def face_detect(frame):
    frame = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.1, 5)

    for (x,y,w,h) in faces:
        print(x, y, w, h)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

    cv2.imshow('face', frame)
    return faces

def cvimage_to_pygame(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return pygame.image.frombuffer(image.tostring(), image.shape[1::-1],
                                   "RGB")

def get_color_pos(mask):
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
 
    # only proceed if at least one contour was found
    if len(cnts) > 0:
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    return center

# pygame show font
def showFont(screen, text, x, y, font_name, size, color):
    if font_name == "simhei":
        font = pygame.font.SysFont(font_name, size)
    else:
        font = pygame.font.Font(font_name, size)
       
    text = font.render(text, 1, color)
    screen.blit(text, (x, y))

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

def pg_resize(img, w, h):
    return pygame.transform.scale(img, (w, h))

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