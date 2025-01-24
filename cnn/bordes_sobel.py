import cv2
import numpy as np

fruta = cv2.imread('img/fruta2.jpg')

kernel_x = np.array([[-1,0,1],
                     [-2,0,2],
                     [-1,0,1]
                     ])

kernel_y = np.array([[-1,-2,-1],
                     [0,0,0,],
                     [1,2,1]
                     ])

kernel_f = np.array([[-2,-2,0],
                     [-2,0,2],
                     [0,2,2]
                     
                     ])

fruta = cv2.cvtColor(fruta, cv2.COLOR_BGR2GRAY)

gx = cv2.filter2D(fruta,-1,kernel_x)
gy = cv2.filter2D(fruta,-1,kernel_y)
gf = cv2.filter2D(fruta,-1,kernel_f)
cv2.imshow('fruta',fruta)
cv2.imshow('gx', gx)
cv2.imshow('gy', gy)
cv2.imshow('gf', gf)

cv2.waitKey(0)