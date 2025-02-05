import cv2
import numpy as np

#Cargar Imagen
carro = cv2.imread('img/carro.jpg')
carro_grices = cv2.cvtColor(carro,cv2.COLOR_RGB2GRAY)
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT,(13,5))

black_hat = cv2.morphologyEx(carro_grices,cv2.MORPH_BLACKHAT,rectKernel)
white_hat = cv2.morphologyEx(carro_grices,cv2.MORPH_TOPHAT,kernel=rectKernel)

cv2.imshow('Original', carro)
cv2.imshow('black_hat',black_hat)
cv2.imshow('white_hat',white_hat)
cv2.waitKey(0)