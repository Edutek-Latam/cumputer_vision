import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img/noise.png',0)


# global thresholding
_,thr1 = cv2.threshold(img,127,255, cv2.THRESH_BINARY)

#Otsu thresholding 
_,thr2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#Otsu despues de aplicar un filtro Gausssian
blur = cv2.GaussianBlur(img,(5,5),0)
_,thr3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)


#mostrar todas las imagenes con matplotlib
images = [img,0,thr1,
          img,0,thr2,
          blur,0,thr3
          ]

titles = ['Original','Histograma','Threshold global',
          'Original','Histograma','Threshold Otsu',
          'Original + Blur','Histograma','Threshold Otsu',
          ]
for i in range(3):
    plt.subplot(3,3,i*3+1), plt.imshow(images[i*3],'gray'),
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])

    plt.subplot(3,3,i*3+2), plt.hist(images[i*3].ravel(),256),
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])

    plt.subplot(3,3,i*3+3), plt.imshow(images[i*3+2],'gray'),
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])

plt.show()
""" cv2.imshow('original',img)
cv2.imshow('thr global',thr1)
cv2.imshow('thr Otsu',thr2)
cv2.imshow('thr Otsu blur',thr3)

cv2.waitKey(0) """