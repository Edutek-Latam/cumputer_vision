#Descriptores SIFT
import cv2
import pandas as pd
import numpy as np

#Cargarmos al imagen
img = cv2.imread('img/stop_base.jpg')

#Se convierte a escala de grices
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Inicializar el detector SIFT
sift = cv2.SIFT_create()

#Obtener los puntos claves o KeyPoints
keypoint = sift.detect(img_gray)

def mostrar_keypoint(imagen,keypoints):
    print("mostrando {} KeyPoints".format(len(keypoints)))
    filas = []

    img_keypoint = cv2.drawKeypoints(imagen,keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow('Original',img)
    cv2.imshow('puntos de interes2',img_keypoint)
    
    cv2.waitKey(0)


mostrar_keypoint(img_gray, keypoint)

