import cv2
import numpy as np

ciudad = cv2.imread('img/flor.jpeg')

ciudad_gray = cv2.cvtColor(ciudad,cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(ciudad_gray,(5,5),0)

edges = cv2.Canny(blur,80,255)

cv2.imshow('grices', ciudad_gray)
cv2.imshow('bordes', edges)
cv2.waitKey(0)