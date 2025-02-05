import cv2
import numpy as np

#Cargar imagen con ruido
carro = cv2.imread('img/noise.png', cv2.IMREAD_GRAYSCALE)

#convertir imagen a una imagen binaria (0 o 1)
binary = cv2.threshold(carro,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

kernel = np.ones((2,2), np.uint8)

open_img = cv2.morphologyEx(binary,cv2.MORPH_OPEN,kernel=kernel)

cv2.imshow('original', carro)
cv2.imshow('Binaria', binary)
cv2.imshow('apertura', open_img)
cv2.waitKey(0)