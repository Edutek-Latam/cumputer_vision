import cv2
import numpy as np

monedas = cv2.imread('img/monedas.jpg')

#convertir a escala de grises
gray = cv2.cvtColor(monedas,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
#cv2.waitKey(0)

#suavizado gaussiano
gauss = cv2.GaussianBlur(gray,(5,5),0)
cv2.imshow('gauss',gauss)
#cv2.waitKey(0)

#Detectamos bordes con Canny
canny = cv2.Canny(gauss,70,200)
cv2.imshow('canny', canny)
cv2.waitKey(0)

#buscamos contornos
(contornos,_) = cv2.findContours(canny.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#print(contornos)

cv2.drawContours(monedas,contornos,-1,(0,0,255),2)
cv2.imshow('contornos', monedas)
cv2.waitKey(0)