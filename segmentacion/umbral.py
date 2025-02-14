import cv2

#cargar la imagen
img = cv2.imread('img/Girasol.jpg')

#Convertir a escala de grices
img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)


#Umbral global
_,imagen_binary = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)

#Umbral Otsu
_,imagen_bin =cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('gray',img_gray)
cv2.imshow('Umbra', imagen_binary)
cv2.imshow('Umbra Otsu', imagen_bin)
cv2.waitKey(0)