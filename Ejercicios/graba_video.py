import cv2 

captura=cv2.VideoCapture(0)
salida=cv2.VideoWriter("VideoSalida.avi",cv2.VideoWriter_fourcc(*"XVid"),20.0,(640,480))
while(captura.isOpened()):
    ret,imagen=captura.read()
    if ret ==True:
        cv2.imshow("Video",imagen)
        salida.write(imagen)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
captura.release()
salida.release()
cv2.destroyAllWindows()