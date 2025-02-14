import cv2
#cargar la imagen
#Segmentacion con Sobel
img = cv2.imread('img/monedas.jpg',0)


edges_prewitt = cv2.GaussianBlur(img,(3,3),0)
cv2.imshow('blur',edges_prewitt)
cv2.waitKey(0)

#Filtro en imagen usando un filtro 2D
filterd_image = cv2.Laplacian(img,ksize=3,ddepth=cv2.CV_16S)

filterd_image = cv2.convertScaleAbs(filterd_image)

cv2.imshow('blur',edges_prewitt)
cv2.imshow('segmento',filterd_image)

cv2.waitKey(0)
