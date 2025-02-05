import cv2
import numpy as np

#Cargar Imagen
carro = cv2.imread('img/noise.png',cv2.IMREAD_GRAYSCALE)
#Convertir imagen a binaria
binary = cv2.threshold(carro,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#definimos Kernel
kernel = np.ones((2,2),np.uint8)

#Operacion Morfologica - close
closing = cv2.morphologyEx(binary,cv2.MORPH_CLOSE, kernel=kernel,iterations=1)

cv2.imshow('Original',carro)
cv2.imshow('Closing', closing)
cv2.waitKey(0)



