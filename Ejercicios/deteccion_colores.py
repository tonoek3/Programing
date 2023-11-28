import cv2
import numpy as np

cap=cv2.VideoCapture(0)

greenBajo1=np.array([0,128,0],np.uint8)
greenAlto1=np.array([8,255,255],np.uint8)

greenBajo2=np.array([0,128,0],np.uint8)
greenAlto2=np.array([179,255,255],np.uint8)


while True:
    ret,frame=cap.read()
    if ret ==True:
        frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        maskRed1=cv2.inRange(frameHSV,greenBajo1,greenAlto1)
        maskRed2=cv2.inRange(frameHSV,greenBajo2,greenAlto2)
        maskRed=cv2.add(maskRed1,maskRed2)
        maskRedvis=cv2.bitwise_and(frame,frame,mask=maskRed)
        cv2.imshow("mascara deteccion verde real",maskRedvis)
        cv2.imshow("mascara deteccion verde",maskRed)
        cv2.imshow("frame",frame)
        if cv2.waitKey(1) & 0xFF ==ord ("q"):
            break

cap.release()
cv2.destroyAllWindows()