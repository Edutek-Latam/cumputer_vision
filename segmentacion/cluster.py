import cv2
import numpy as np

#Segmentacion por K-means clustering

img = img = cv2.imread('img/Girasol.jpg')
#Convertimos la imgaen a un espacio de colores 
lab_image = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)

pixels = lab_image.reshape((-1,3))

#Aplicamos K-means
k = 3  #Numero de clusters (colores principales)

_,labels,centers = cv2.kmeans(np.float32(pixels),k,None,(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,10,1.0),10,cv2.KMEANS_RANDOM_CENTERS)

segment_img = np.uint8(centers[labels.flatten()].reshape(img.shape))
segment_img_bgr = cv2.cvtColor(segment_img,cv2.COLOR_LAB2BGR)
""" cv2.imshow('original',img)
#cv2.imshow('colores lab', lab_image)
cv2.imshow('img_seg', segment_img_bgr)

cv2.waitKey(0) """

##########################################
### Segmentacion por mean shift

mean_shift = cv2.pyrMeanShiftFiltering(img,15,15,maxLevel=0)
""" cv2.imshow('mean', mean_shift)
cv2.imshow('Original', img)
cv2.waitKey(0) """


#########################################33
##### Segmentacion con Watershed


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#convertir a imagen binaria
_,img_bin = cv2.threshold(gray, 127,255,cv2.THRESH_BINARY)

#Crear un kernel de 3x3 -> de unos
kernel = np.ones((3,3))

opening = cv2.morphologyEx(img_bin, cv2.MORPH_CLOSE,kernel=kernel, iterations=1)

contorno,_ = cv2.findContours(opening,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

markers = np.zeros(img.shape[:2],np.int32) #int32 para los markers

for i, contor in enumerate(contorno):
    cv2.drawContours(markers,contorno,i, i+1,-1)

segment_img = cv2.watershed(img.astype(np.uint8),markers)
segment_img = np.uint8(segment_img)

cv2.imshow('original',img)
cv2.imshow('segmentada',segment_img)
cv2.waitKey(0)
