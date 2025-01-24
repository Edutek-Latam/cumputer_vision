import cv2
import numpy as np

vertical = cv2.imread('img/Vertical.png')

kernel_x = np.array([[-1,1],
                     [0,0]])

kernel_y = np.array([[-1,0],
                     [1,-0]])

output_x = cv2.filter2D(vertical,-1,kernel_x)
output_y = cv2.filter2D(vertical,-1,kernel_y)

""" cv2.imshow('vertical',vertical)
cv2.imshow('vertical_x',output_x)
cv2.imshow('vertical_y',output_y)
 """

horizontal = cv2.imread('img/Horizontal.png')
gx= cv2.filter2D(horizontal,-1,kernel_x)
gy = cv2.filter2D(horizontal,-1,kernel_y)
""" 
cv2.imshow('horizontal', horizontal)
cv2.imshow('gx', gx)
cv2.imshow('gy',gy)
cv2.waitKey(0)
 """

fruta = cv2.imread('img/fruta2.jpg')
gx= cv2.filter2D(fruta,-1,kernel_x)
gy = cv2.filter2D(fruta,-1,kernel_y)
cv2.imshow('fruta', fruta)
cv2.imshow('gx', gx)
cv2.imshow('gy',gy)
cv2.waitKey(0)