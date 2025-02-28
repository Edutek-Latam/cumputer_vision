#Cambiar color o escala de colores a una imagen
import skimage as ski
import matplotlib.pyplot as plt
import cv2
original = ski.data.astronaut()

#OpenCV
#gray = cv2.cvtColor(original,cv2.COLOR_BAYER_BG2GRAY)
gray = ski.color.rgb2gray(original)

fig,axes = plt.subplots(1,2)
ax = axes.ravel()

ax[0].imshow(original)
ax[0].set_title('Original')

ax[1].imshow(gray,cmap=plt.cm.gray)
ax[1].set_title('Grayscale')


plt.show()
#ski.io.imshow(gray)
#ski.io.show()