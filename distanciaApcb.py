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

    # For each detection
    for *box, conf, cls in result.xyxy[0]:
        # Get the center of the bounding box
        x_center = int((box[0] + box[2]) / 2)
        y_center = int((box[1] + box[3]) / 2)

        # Move the cursor to the center of the bounding box
        point = (x_center, y_center)

        # Show distance for a specific point
        cv2.circle(color_frame, point, 4, (0, 0, 255))
        distance = depth_frame[point[1], point[0]]

        cv2.putText(color_frame, "{}mm".format(distance), (point[0], point[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

    # Show frames
    cv2.imshow("Color frame", color_frame)

    # Close program
    key = cv2.waitKey(1)
    if key == 27:
        break

dc.release()
cv2.destroyAllWindows()

