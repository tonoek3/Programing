from ultralytics import YOLO
import cv2

# Read model
model = YOLO("best3.pt")

# Capture video
cap = cv2.VideoCapture(1)

while True:
    # Read frames
    ret, frame = cap.read()

    # Read results
    result = model.predict(frame, imgsz = 640, conf = 0.85)

    # Show results
    labels = result[0].plot()

    # For each detection
    for *box, conf, cls in result:
        # Get the center of the bounding box
        x_center = int((box[0] + box[2]) / 2)
        y_center = int((box[1] + box[3]) / 2)

        # Draw a circle at the center of the bounding box
        cv2.circle(frame, (x_center, y_center), 4, (0, 0, 255), -1)

    # Show frames
    cv2.imshow("Detect and Segmentation", frame)

    # Close program
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()