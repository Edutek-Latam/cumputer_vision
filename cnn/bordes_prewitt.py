import cv2
import numpy as np

fruta = cv2.imread('img/fruta2.jpg')

kernel_x = np.array([[-1,0,1],
                     [-1,0,1],
                     [-1,0,1]
                     ])

kernel_y = np.array([[-1,-1,-1],
                     [0,0,0,],
                     [1,1,1]
                     ])

fruta = cv2.cvtColor(fruta, cv2.COLOR_BGR2GRAY)

output_x = cv2.filter2D(fruta,-1,kernel_x)
output_y = cv2.filter2D(fruta,-1,kernel_y)

cv2.imshow('fruta',fruta)
cv2.imshow('X', output_x)
cv2.imshow('y', output_y)
cv2.waitKey(0)