import cv2
import numpy as np

imagen = cv2.imread('img/letras.jpg', cv2.IMREAD_GRAYSCALE)

#Definimos el porcentaje el cambio de tamano
scale_porcent = 10
print(imagen.shape)
#Cambiar tamano de imagen
#definir el ancho de la imagen, shape devuelve las dimensiones
width = int(imagen.shape[0] * scale_porcent/100)
height = int(imagen.shape[1] * scale_porcent/100)

#resize image
imagen_resized = cv2.resize(imagen,(width, height), interpolation=cv2.INTER_AREA)

_,binary_image = cv2.threshold(imagen_resized,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

kenel = np.ones((5,5),np.uint8)

invert = cv2.bitwise_not(binary_image)

erosion = cv2.erode(invert,kernel=kenel,iterations=1)
cv2.imshow('Original', imagen_resized)
cv2.imshow('Binaria', invert)
cv2.imshow('Erosion', erosion)
cv2.waitKey(0)