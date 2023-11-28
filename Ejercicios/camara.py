import cv2 

captura=cv2.VideoCapture(0)

while(captura.isOpened()):
    ret,imagen=captura.read()
    if ret ==True:
        cv2.imshow("Video",imagen)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
captura.release()
cv2.destroyAllWindows()
