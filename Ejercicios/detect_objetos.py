import cv2 
import numpy as np

cap=cv2.VideoCapture(0)
#image=cv2.imread(0)

while True:
    ret,frame=cap.read()
    if ret == True:
        cv2.imshow("Video", frame)
        if cv2.waitKey(1)& 0xFF == ord ("q"):
            break

cap.release()
cv2.destroyAllWindows()

