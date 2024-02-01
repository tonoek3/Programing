"""import cv2
import numpy as np

# Iniciar la captura de video
cap = cv2.VideoCapture(1)

while True:
    # Leer un frame de la cámara
    _, imagen = cap.read()

    # Convertir la imagen a espacio de color HSV
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

    # Definir el rango de color verde en HSV
    verde_bajo = np.array([35, 100, 100], dtype=np.uint8)
    verde_alto = np.array([85, 255, 255], dtype=np.uint8)

    # Crear una máscara con solo los píxeles dentro del rango de verde
    mascara = cv2.inRange(hsv, verde_bajo, verde_alto)

    # Encontrar los contornos en la máscara
    contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contorno in contornos:
        # Calcular el centroide del contorno
        momentos = cv2.moments(contorno)
        if momentos["m00"] != 0:
            cX = int(momentos["m10"] / momentos["m00"])
            cY = int(momentos["m01"] / momentos["m00"])
        else:
            cX, cY = 0, 0

        # Dibujar un punto en el centroide
        cv2.circle(imagen, (cX, cY), 5, (255, 255, 255), -1)

    # Mostrar la imagen
    cv2.imshow('Imagen', imagen)

    # Si se presiona la tecla 'q', salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y destruir todas las ventanas
cap.release()
cv2.destroyAllWindows()"""

############################################################################

"""import cv2
import numpy as np

# Iniciar la captura de video
cap = cv2.VideoCapture(1)

while True:
    # Leer un frame de la cámara
    _, imagen = cap.read()

    # Convertir la imagen a espacio de color HSV
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

    # Definir el rango de color verde en HSV
    # Ajusta estos valores para que coincidan con el tono de verde de la PCB
    verde_bajo = np.array([35, 100, 100], dtype=np.uint8)
    verde_alto = np.array([85, 255, 255], dtype=np.uint8)

    # Crear una máscara con solo los píxeles dentro del rango de verde
    mascara = cv2.inRange(hsv, verde_bajo, verde_alto)

    # Encontrar los contornos en la máscara
    contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Verificar si se encontraron contornos antes de proceder
    if contornos:
        # Suponemos que la PCB es el contorno más grande en la imagen
        contorno_pcb = max(contornos, key=cv2.contourArea)

        # Calcular el centroide del contorno de la PCB
        momentos = cv2.moments(contorno_pcb)
        if momentos["m00"] != 0:
            cX = int(momentos["m10"] / momentos["m00"])
            cY = int(momentos["m01"] / momentos["m00"])
        else:
            cX, cY = 0, 0

        # Dibujar un punto en el centroide de la PCB
        cv2.circle(imagen, (cX, cY), 5, (255, 255, 255), -1)

    # Mostrar la imagen
    cv2.imshow('Imagen', imagen)

    # Si se presiona la tecla 'q', salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y destruir todas las ventanas
cap.release()
cv2.destroyAllWindows()"""


###################################################################################################33

from ultralytics import YOLO
import cv2

# Leer el modelo
model = YOLO("best3.pt")

# Iniciar la captura de video
cap = cv2.VideoCapture(1)

while True:
    # Leer un frame de la cámara
    ret, frame = cap.read()

    # Verificar si el frame se capturó correctamente
    if not ret:
        print("No se pudo capturar el frame")
        continue

    # Predecir los objetos en el frame
    result = model.predict(frame, imgsz=640, conf=0.85)

    # Iterar sobre cada objeto detectado
    for obj in result[0].objects:
        # Calcular el centroide del objeto
        cX = int(obj.xyxy[0] + (obj.xyxy[2] - obj.xyxy[0]) / 2)
        cY = int(obj.xyxy[1] + (obj.xyxy[3] - obj.xyxy[1]) / 2)

        # Dibujar un punto en el centroide del objeto
        cv2.circle(frame, (cX, cY), 5, (255, 255, 255), -1)

    # Mostrar la imagen
    cv2.imshow('Imagen', frame)

    # Si se presiona la tecla 'q', salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y destruir todas las ventanas
cap.release()
cv2.destroyAllWindows()






