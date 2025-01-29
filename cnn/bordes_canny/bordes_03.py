import cv2

imagen = cv2.imread('img/flor.jpeg',cv2.IMREAD_GRAYSCALE)

cv2.namedWindow('Canny')

def nothing(x):
    pass


#Crear barras para ajustar
cv2.createTrackbar('Trheshold 1','Canny',50,255,nothing)
cv2.createTrackbar('Trheshold 2','Canny',150,255,nothing)


while True:
    trheshold1 = cv2.getTrackbarPos('Trheshold 1','Canny')
    trheshold2 = cv2.getTrackbarPos('Trheshold 2','Canny')

    egdes = cv2.Canny(imagen,trheshold1,trheshold2)

    cv2.imshow('Canny',egdes)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()



