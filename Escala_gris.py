import numpy as np
import cv2

cap= cv2.VideoCapture(0)

while(True):
    ret, frame=cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)

    cv2.imshow("Visor",gray)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()