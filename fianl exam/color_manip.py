import cv2
import numpy as np

def RGB2HSV(ref):
    refBGR=np.uint8([[[ref[2],ref[1],ref[0]]]])
    refHSV = cv2.cvtColor(refBGR,cv2.COLOR_BGR2HSV)
    return refHSV[0][0][0]
def color_detect(img, color, thres=30, it=2, inv=False): # rgb
    lower_Hue = None
    upper_Hue = None
    if color=='skin':
        lower_Hue = np.array([0, 48, 80], dtype=np.uint8)
        upper_Hue = np.array([20, 255, 255], dtype=np.uint8)
    elif color=='black':
        lower_Hue = np.array([0, 0, 0])
        upper_Hue = np.array([thres, thres, thres])
    else:
        hue = RGB2HSV(color)
        lower_Hue = np.array([hue-thres, 50, 50], dtype=np.uint8)
        upper_Hue = np.array([hue+thres, 255, 255], dtype=np.uint8)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_Hue, upper_Hue)
    # kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (11, 11))
    # mask
    mask = cv2.erode(mask, kernel, iterations=it)
    mask = cv2.dilate(mask, kernel, iterations=it)
    mask_inv = cv2.bitwise_not(mask)
    # result
    if inv:
        res = cv2.bitwise_and(img, img, mask=mask_inv)
    else:
        res = cv2.bitwise_and(img, img, mask=mask)
    return (res, mask, mask_inv)

# img       -> 圖
# det_color -> 偵測的顏色
# to        -> 更換的顏色
def color_chg(img, det_color, to, thres=30, it=2, inv=True): #rgb
    fullcolor = np.full(frame.shape, (to[2], to[1], to[0]), dtype=np.uint8)
    img, mask, mask_inv = color_detect(img, det_color, thres, it, inv)
    fg = cv2.bitwise_and(fullcolor, fullcolor, mask=mask)
    bg = cv2.bitwise_and(frame, frame, mask=mask_inv)
    final = cv2.add(fg, bg)
    return final