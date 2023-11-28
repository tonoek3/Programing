import cv2
import numpy as np

cap=cv2.VideoCapture(0)

azulBajo=np.array([100,100,20],np.uint8)
azulAlto=np.array([125,255,255],np.uint8)

amarilloBajo=np.array([0,128,0],np.uint8)
amarilloAlto=np.array([125,255,255],np.uint8)

greenBajo1=np.array([0,128,0],np.uint8)
greenAlto1=np.array([8,255,255],np.uint8)

greenBajo2=np.array([0,128,0],np.uint8)
greenAlto2=np.array([179,255,255],np.uint8)

while True:
    ret,frame=cap.read()
    if ret ==True:
        frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mask=cv2.inRange(frameHSV,azulBajo,azulAlto)
        contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame,contornos,-1,(255,0,0),2)
        cv2.imshow("Detect azul",mask)
        for c in contornos:
            area=cv2.contourArea(c)
            if area > 1500:
                M=cv2.moments(c)
                if (M["m00"]==0): M["m00"]=1
                x= int(M["m10"]/M["m00"])
                y= int(M["m01"]/M["m00"])
                cv2.circle(frame,(x,y),7,(0,255,0),1)
                fort = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame,"{},{}".format(x,y),(x+10,y),fort,0.75,(0,255,0),1,cv2.LINE_AA)
                nuevoContorno=cv2.convexHull(c)
                cv2.drawContours(frame,[nuevoContorno],0,(255,0,0),2)

        cv2.imshow("imagen de video",frame)
        if cv2.waitKey(1) & 0xFF ==ord ("q"):
            break

cap.release()
cv2.destroyAllWindows()

