import  cv2
import numpy
from matplotlib import pyplot as plt

img = cv2.imread('img/image22.png', cv2.IMREAD_GRAYSCALE)
img = cv2.medianBlur(img,5)


#Imangen con threshold global
_,thre1 = cv2.threshold(img,127,255, cv2.THRESH_BINARY)

#img= recibimos una imagen
#255 = maxValue = el valor máximo que se asignan a los pixeles que superan el umbral o threshold
#ADAPTIVE_THRESH_MEAN_C = Calcula como una suma ponderada de los valores de los pixeles vecinos definido por el blocksize menos la constante C
#THRESH_BINARY = thresholdType = el tipo de threshold que vamos a utilizar

#BlockSize = el tamaño del vecindario o kernel  a utilizar para calcular el umbral por cada pixel, este debe de ser un valor entero impar
#C= es una constante que se resta o suma a la media ponderada calculada, 
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

#ADAPTIVE_THRESH_GAUSS = Una media ponderada gaussiana, los pixeles mas cercanos al centro tienen mayor peso
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

titles = ['Original','Global Threshol(v=127)','Adaptative MEAN','Adaptative Gaussian']

images =[img,thre1,th2,th3]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()


""" cv2.imshow('orig', img)
cv2.imshow('trh1', thre1)
cv2.imshow('trh2', th2)
cv2.imshow('trh3', th3)

cv2.waitKey(0)
 """