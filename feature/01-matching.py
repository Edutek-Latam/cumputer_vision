"""
Feature Matching
"""
import cv2

#Carga de imagenes
img1 = cv2.imread('img/zelda_01.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('img/zelda_02.png', cv2.IMREAD_GRAYSCALE)

#Inicializar el detector SIFT
sift = cv2.SIFT_create()

#Encontrar los puntos claves y descriptores SIFT
kp1,des1 = sift.detectAndCompute(img1,None)
kp2,des2 = sift.detectAndCompute(img2,None)

#Inizializar el matcher BFMatcher (Brute-Force Matcher)
bf =cv2.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2)

good_matches = []

for m,n in matches:
    if m.distance < 0.30 * n.distance:
        good_matches.append([m])

#Dibujar las coincidencias
img_matches = cv2.drawMatchesKnn(img1,kp1,img2,kp2, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

cv2.imshow('Conincidencias SIFT', img_matches)
cv2.waitKey(0)
cv2.destroyAllWindows()