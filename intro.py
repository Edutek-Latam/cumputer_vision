import cv2
import numpy as np
import matplotlib.pyplot as plt
bananos = cv2.imread("img/flores.jpg")

#canales RGB
print(bananos[0,0,:])


#opencv lo toma como BGR
b=bananos[:,:,0]
g=bananos[:,:,1]
r=bananos[:,:,2]
#cv2.imshow("",g)
#cv2.waitKey(0)
#cv2.distroyAllwindows()
#crear canal en color negro
negro= np.zeros_like(b)

#hacer un merge de cada canal
canal_azul = cv2.merge((b,negro,negro))

#hacer un merge de cada canal
canal_verde = cv2.merge((negro,g,negro))


canal_rojo = cv2.merge((negro,negro,r))
""" 
cv2.imshow("",canal_azul)
cv2.waitKey(0)

cv2.imshow("",canal_verde)
cv2.waitKey(0)


cv2.imshow("",canal_rojo)
cv2.waitKey(0) """

img_gray = cv2.cvtColor(bananos,cv2.COLOR_BGR2GRAY)
#cv2.imshow("",img_gray)
#cv2.waitKey(0)

freq,bins,patches = plt.hist(img_gray.flatten(), bins=15)
plt.show()

img_binary = np.uint8(255 * (img_gray < 233))#

print(img_binary)
cv2.imshow('img_binary',img_binary)
cv2.waitKey(0)
#img_binary = np.uint8()

img_segmentada =  np.uint8(img_gray * (img_binary/255))
""" cv2.imshow('',img_segmentada)
cv2.waitKey(0) """

#se debe de realizar la operacion por cada canal
seg_color = bananos.copy()
#redimenziar la imagen, si muestra un error de la dimension
img_binary_rezised = cv2.resize(img_binary,(seg_color.shape[1], seg_color.shape[0]))

seg_color[:,:,0] = np.uint8(b * (img_binary_rezised/255))
seg_color[:,:,1] = np.uint8(g * (img_binary_rezised/255))
seg_color[:,:,2] = np.uint8(r * (img_binary_rezised/255))
""" cv2.imshow('',seg_color)
cv2.waitKey(0)
 """

th_otsu,_ = cv2.threshold(img_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
binario_otsu = np.uint8(255 * (img_gray< th_otsu))
cv2.imshow('otsu', binario_otsu)
cv2.waitKey(0)

