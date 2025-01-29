import cv2
import numpy as np

imagen = cv2.imread('img/flor.jpeg')

#suavizado gaussiano
gauss = cv2.GaussianBlur(imagen,(5,5),3)
cv2.imshow('gauss',gauss)

cv2.imshow('Gauss', gauss)
cv2.waitKey(0)