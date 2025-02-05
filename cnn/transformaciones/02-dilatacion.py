import cv2
import numpy as np

#cargar imagen, en escala de grices
imagen = cv2.imread('img/letras.jpg',0)


#Definimos el porcentaje el cambio de tamano
scale_porcent = 10
print(imagen.shape)
#Cambiar tamano de imagen
#definir el ancho de la imagen, shape devuelve las dimensiones
width = int(imagen.shape[0] * scale_porcent/100)
height = int(imagen.shape[1] * scale_porcent/100)

#resize image
imagen_resized = cv2.resize(imagen,(width, height), interpolation=cv2.INTER_AREA)


_,binary = cv2.threshold(imagen_resized,127,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

kernel = np.ones((4,4), np.uint8)

invert = cv2.bitwise_not(binary)
dilatacion = cv2.dilate(invert,kernel=kernel,iterations=1)

cv2.imshow('Original',invert)
cv2.imshow('Dilatacion',dilatacion)

cv2.waitKey(0)

