import cv2
import numpy as np

def nothing(x):
		pass
class TrackBar():
	def __init__(self, window, barName):
		cv2.namedWindow(window)
		cv2.createTrackbar(barName, window, 100, 255, nothing)
		self.window = window
		self.barName = barName
	def getTrackbarPos(self):
		return cv2.getTrackbarPos(self.barName, self.window)