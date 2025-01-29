import cv2 
import numpy as np

imagen = cv2.imread('img/flor.jpeg')

kernel_gauss = np.array([[1,1,1],
                         [1,1,1],
                         [1,1,1]],np.float32)/9
output = cv2.filter2D(imagen,-1,kernel_gauss)

kernel_sobel_x = np.array([[-1,0,1],
                           [-2,0,2],
                           [-1,0,1]
                           ])
imagen_bordes = cv2.filter2D(imagen,-1,kernel_sobel_x)
cv2.imshow('bordes',imagen_bordes)
cv2.waitKey(0)
