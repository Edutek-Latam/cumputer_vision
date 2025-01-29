import cv2
import numpy as np

img = cv2.imread('img/ciudad.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#gray = np.float32(img)

output = cv2.cornerHarris(gray,blockSize=2,ksize=5,k=0.04)

output = cv2.dilate(output,None)
trheshold = 0.001 * output.max()

img[output > trheshold] = [0,0,255]




imagen = cv2.imread('img/ciudad.jpg')
gray = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,2000,0.01,10)

corners = np.intp(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(imagen,(x,y),3,255,-1)


cv2.imshow('img_gray',img)
cv2.imshow('img_gray2',imagen)
cv2.waitKey(0)
"""
#
output = cv2.dilate(output,None)

 """




