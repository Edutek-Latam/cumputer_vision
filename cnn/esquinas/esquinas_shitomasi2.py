import cv2 
import numpy as np

#imagen = cv2.imread('img/ciudad.jpg')
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    if not ret:
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray,2000,0.01,10)
    corners = np.intp(corners)

    blank_img = np.zeros((frame.shape[0],frame.shape[1],3),np.uint8)

    for i in corners:
        x,y = i.ravel()
        cv2.circle(blank_img,(x,y),3,255,-1)

    cv2.imshow('real time',blank_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



