from ultralytics import YOLO
import cv2

#Read model
model = YOLO("best.pt")

#Capture video
cap = cv2.VideoCapture(1)

while True:
    #Read frames
    ret, frame = cap.read()

    #Read results
    result = model.predict(frame, imgsz = 640, conf = 0.85)

    #Show results
    labels = result[0].plot()

    #Show frames
    cv2.imshow("Detect and Segmentation", labels)

    #Close program
    if cv2.waitKey(1) ==27:
        break

cap.release()
cv2.destroyAllWindows()
