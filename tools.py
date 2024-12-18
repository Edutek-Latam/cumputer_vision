import cv2
imagen = cv2.imread("img/bananos.jpg")

ancho,alto = int(imagen.shape[1]* 0.5),int(imagen.shape[0]*0.5)
imagen_2 = cv2.resize(imagen,(ancho,alto))
cv2.imshow('',imagen)
cv2.waitKey(0)
imagen_rotada = cv2.rotate(imagen,cv2.ROTATE_180)
cv2.imshow('imagen rotada', imagen_rotada)
cv2.waitKey(0)
