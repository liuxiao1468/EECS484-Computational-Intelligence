import cv2, sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def increase_brightness(img, value=0):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

def cannyEdge(img):
	minT = 250
	maxT = 255
	edge = cv2.Canny(img, minT, maxT)
	cv2.imshow("edge",edge)
	return edge



img = cv2.imread('img.png')


cv2.imshow('original img',img)
print ('original',img)
img = increase_brightness(img, value=50)
print ('after preprocessing',img)
cv2.imshow('img',img)
cv2.imwrite('img_pre1.png',img)

edge= cannyEdge(img)
shape=edge.shape
print('edges',shape)
print(edge)


cv2.imwrite('img_pre2.png',edge)
cv2.waitKey(0)
cv2.destroyAllWindows()


