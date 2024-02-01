import cv2
from pyrealsense2 import *
from realsense_depth import *
from ultralytics import YOLO

# Initialize Camera Intel Realsense
dc = DepthCamera()

# Read model
model = YOLO("best3.pt")

while True:
    ret, depth_frame, color_frame = dc.get_frame()

    # Read results
    result = model.predict(color_frame, imgsz = 640, conf = 0.85)

    # Show results
    labels = result[0].plot()

    # For each detection
    for det in result[0].boxes:
        # Get the center of the bounding box
        x_center = int((det[0] + det[2]) / 2)
        y_center = int((det[1] + det[3]) / 2)

        # Show distance for a specific point
        cv2.circle(labels, (x_center, y_center), 4, (0, 0, 255))
        distance = depth_frame[y_center, x_center]

        cv2.putText(labels, "{}mm".format(distance), (x_center, y_center - 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

    # Show frames
    cv2.imshow("Color frame", labels)

    # Close program
    key = cv2.waitKey(1)
    if key == 27:
        break

dc.release()
cv2.destroyAllWindows()