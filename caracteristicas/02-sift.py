import cv2
import matplotlib.pyplot as plt
import numpy as np


#Cargar  imagenes
img_referencia = cv2.imread('img/stop_base.jpg', cv2.IMREAD_GRAYSCALE)
img_busqueda = cv2.imread('img/stop_signal.jpg', cv2.IMREAD_GRAYSCALE)

#Inicializar SIFT
#Crear un objeto detector SIFT. Este objeto se utilizara para encontrar puntos claves o KeyPoints

sift = cv2.SIFT_create()

#Encontrar los puntos claves y descriptores
#Esta funcion encuentra los puntos claves y calcula los dresciptores 
kp1, des1 = sift.detectAndCompute(img_referencia, None)
kp2, des2 = sift.detectAndCompute(img_busqueda, None)

bf = cv2.BFMatcher()

#k: Encuentra los 2 vecinos más cercanos
matches = bf.knnMatch(des1,des2, k=2)

good_matches =[]

for m,n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append(m)

src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1,1,2)
dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1,1,2)

M,mask = cv2.findHomography(src_pts, dst_pts,cv2.RANSAC,5.0)


#Obtener las dimensiones del objeto de referencia
h,w = img_referencia.shape

pts = np.float32([[0,0],[0,h -1],[w-1,h-1],[w-1,0]]).reshape(-1,1,2)
dst = cv2.perspectiveTransform(pts, M)

img_busqueda_rgb = cv2.cvtColor(img_busqueda,cv2.COLOR_GRAY2RGB)
cv2.polylines(img_busqueda_rgb,[np.int32(dst)],True,(0,255,0),3,cv2.LINE_AA)

plt.figure(figsize=(10,10))
plt.imshow(img_busqueda_rgb)
plt.title('Objeto detectado')
plt.show()