import cv2 
import numpy as np

gato = cv2.imread('img/fruta2.jpg')

kernel_3x3 = np.ones((3,3))/(3*3)
#print(kernel_3x3)
output_3x3 = cv2.filter2D(gato,-1,kernel_3x3)

kernel_10x10 = np.ones((10,10))/(10*10)
output_10x10 = cv2.filter2D(gato,-1,kernel_10x10)

kernel_30x30 = np.ones((30,30))/(30*30)
output_30x30 = cv2.filter2D(gato,-1,kernel_30x30)

""" cv2.imshow('Gato', gato)
cv2.imshow('Gato 3x3', output_3x3)
cv2.imshow('Gato 10x10', output_10x10)
cv2.imshow('Gato 30x30', output_30x30)
cv2.waitKey(0) """

kernel_bordes = np.array([[-1,-1,-1],
                          [-1,8,-1],
                           [-1,-1,-1]
                          ])
output_bordes = cv2.filter2D(gato,-1, kernel_bordes)
cv2.imshow('bordes', output_bordes)
cv2.imshow('gato', gato)
"""
cv2.waitKey(0) """

img2 = cv2.imread('img/vector.png')

kernel_x = np.array([[1,0,-1],
                     [1,0,-1],
                     [1,0,-1]
                     ])

output_x = cv2.filter2D(img2,-1,kernel_x)
""" cv2.imshow('output_x',output_x)
cv2.imshow('img',img2) """
#cv2.waitKey(0)
 

kernel_y = np.array([[1,1,1],
                     [0,0,0],
                     [-1,-1,-1]])

""" output_y = cv2.filter2D(img2,-1,kernel_y)
cv2.imshow('output_y', output_y);
cv2.waitKey(0) """

""" 
cv2.imshow('vectores',img2)
cv2.waitKey() """

gray = cv2.cvtColor(gato,cv2.COLOR_BGR2GRAY)
gx = cv2.Sobel(gray,cv2.CV_64F,1,0,5)
gy = cv2.Sobel(gray,cv2.CV_64F,0,1,5)

mag,_=cv2.cartToPolar(gx,gy)
mag = np.uint8(255*mag/np.max(mag))

cv2.imshow('bordes Sobel',mag)
cv2.waitKey(0)


