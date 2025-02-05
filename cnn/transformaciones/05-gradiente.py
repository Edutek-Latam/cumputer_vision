import cv2
import numpy as np

#Cargar Imagen
letras = cv2.imread('img/letras2.jpg',cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5,5),np.uint8)

#Aplicar la dilatacion
dilation = cv2.dilate(letras,kernel=kernel, iterations=1)

#Aplicar la erosion
erosion = cv2.erode(letras,kernel=kernel,iterations=1)

#Gradiente
gradient = dilation - erosion

cv2.imshow('original',letras)
cv2.imshow('gradient',gradient)

cv2.waitKey(0)
