import cv2
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
#cv2.IMREAD_GRAYSCALE carga la imagen en escala de grices
img_gray = cv2.imread('img/Girasol.jpg',cv2.IMREAD_GRAYSCALE)

#cv2.IMREAD_UNCHANGED carga la imagen con los colores y si tienen canales alfa los carga tambien
img_unchanged = cv2.imread('img/Girasol.jpg',cv2.IMREAD_UNCHANGED)

#cv2.IMREAD_COLOR carga la imagen con el color
img_color = cv2.imread('img/Girasol.jpg',cv2.IMREAD_COLOR)

""" cv2.imshow('img_gray', img_gray)
cv2.imshow('unchanged', img_unchanged)
cv2.imshow('color', img_color)
cv2.waitKey(0)
 """


####################################
#Threshold

#
img2 = cv2.imread('img/fruta2.jpg',cv2.IMREAD_GRAYSCALE)
#img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
escala = 0.2
height,width = img2.shape

dim = (int(width*escala), int(height*escala))
#print(dim)
img_rezised = cv2.resize(img2,dim,interpolation=cv2.INTER_AREA)

#cv2.THRESH_BINARY: Si el valor del pixel es mayor al umbral, se asigna el valor maxval, de lo contrario se asigna 0
_,thresh1 = cv2.threshold(img_rezised,127,255,cv2.THRESH_BINARY)

#THRESH_BINARY_INV: Si el valor del pixel es mayor al umbral,se asigna 0, de lo contrario se asigna maxval
_,thresh2 = cv2.threshold(img_rezised,127,255,cv2.THRESH_BINARY_INV)

#THRESH_TRUNC: Si el valor del pixel es mayor que el umbral, se trunca al valor del umbral, de lo contrario no se modifica
_,thresh3 = cv2.threshold(img_rezised,100,255,cv2.THRESH_TRUNC)

#THRESH_TOZERO: Si el valor del pixel es mayor al umbral, no se modifica, de lo contrario se asigna 0
_,thresh4 = cv2.threshold(img_rezised,50,255,cv2.THRESH_TOZERO)

#THRESH_TOZERO_INV:Si el valor del pixel es mayor que el del umbral se asigna a 0, de lo contrario no se modifica 
_,thresh5 = cv2.threshold(img_rezised,50,255,cv2.THRESH_TOZERO_INV)



##### Mostrar con matplotlib las 6 imagenes
""" titulos = ['original','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img_rezised,thresh1,thresh2,thresh3,thresh4,thresh5]

plt.figure(figsize=(8,8))

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray',vmin=0,vmax=300)
    plt.title(titulos[i])
    plt.xticks([])
    plt.yticks([])
plt.show() """

##### Mostrar las imagenes con OpenCV
""" cv2.imshow('imagen', img_rezised)
cv2.imshow('THRESH_BINARY',thresh1)
cv2.imshow('THRESH_BINARY_INV',thresh2)
cv2.imshow('THRESH_TRUNC',thresh3)
cv2.imshow('THRESH_TOZERO',thresh4)
cv2.imshow('THRESH_TOZERO_INV',thresh5)

cv2.waitKey(0) """


img3 = cv2.imread('img/noise.png',0)
# global thresholding
_,thr1 = cv2.threshold(img3,127,255, cv2.THRESH_BINARY)





