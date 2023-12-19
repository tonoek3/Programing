from ultralytics import YOLO
import cv2
import numpy as np

# Leer modelos
model = YOLO("bestUSB.pt")
model2 = YOLO("best3.pt")

# Capturar video
cap = cv2.VideoCapture(0)

while True:
    # Leer frames
    ret, frame = cap.read()

    # Realizar predicciones
    result = model.predict(frame, imgsz=640, conf=0.99)
    result2 = model2.predict(frame, imgsz=640, conf=0.90)

    # Mostrar resultados
    labels = result[0].plot()
    labels2 = result2[0].plot()

    # Combinar resultados
    combined = cv2.addWeighted(labels, 0.4, labels2, 0.4, .5)

    # Mostrar frames
    cv2.imshow("Detección y Segmentación", combined)

    # Cerrar programa
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
