import cv2 
import numpy as np

imagen = cv2.imread('img/ciudad.jpg')
gray = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,2000,0.01,10)

corners = np.intp(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(imagen,(x,y),3,255,-1)

cv2.imshow('Shi-tomasi',imagen)
cv2.waitKey(0)