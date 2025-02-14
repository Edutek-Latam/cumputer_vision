#Segmentacion por bordes

import cv2
#cargar la imagen
#Segmentacion con Sobel
img = cv2.imread('img/monedas.jpg',0)

sobel_x = cv2.Sobel(img,cv2.CV_64F,1,0, ksize=3)

sobel_y = cv2.Sobel(img,cv2.CV_64F,0,1, ksize=3)

sobel_final = cv2.magnitude(sobel_x,sobel_y)

""" cv2.imshow('sobel_x', sobel_x)
cv2.imshow('sobel_y', sobel_y)
cv2.imshow('final', sobel_final)
cv2.waitKey(0) """

#Segmentacion por bordes con Canny

""" edges = cv2.Canny(img,100,200)
cv2.imshow('Canny egdes', edges)
cv2.waitKey(0) """

#Segmentacion por Prewitt
#Reducir el ruido en la imagen




