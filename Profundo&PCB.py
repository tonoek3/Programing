import cv2
from pyrealsense2 import *
from realsense_depth import *
from ultralytics import YOLO

point = (400, 300)

def show_distance(event, x, y, args, params):
    global point
    point = (x, y)

# Initialize Camera Intel Realsense
dc = DepthCamera()

# Create mouse event
cv2.namedWindow("Color frame")
cv2.setMouseCallback("Color frame", show_distance)

# Read model
model = YOLO("best3.pt")

while True:
    ret, depth_frame, color_frame = dc.get_frame()

    # Show distance for a specific point
    cv2.circle(color_frame, point, 4, (0, 0, 255))
    
    distance = depth_frame[point[1], point[0]]

    # cv2.putText(color_frame, "{}mm".format(distance), (point[0], point[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

    # Read results
    result = model.predict(color_frame, imgsz = 640, conf = 0.85)

    # Show results
    if len(result) > 0:
        labels = result[0].plot()
        x = float(result[0].boxes.xywh[0][0])
        y = float(result[0].boxes.xywh[0][1])
        w = float(result[0].boxes.xywh[0][2])
        h = float(result[0].boxes.xywh[0][3])
        x_center = x + w/2
        y_center = y + h/2
        new_point = (x_center, y_center)
        new_distance = depth_frame[new_point[1], new_point[0]]

        cv2.putText(color_frame, "{}mm".format(new_distance), (new_point[0], new_point[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
    # Show frames
    cv2.imshow("Color frame", labels)

    # Close programq
    key = cv2.waitKey(1)
    if key == 27:
        break

dc.release()
cv2.destroyAllWindows()


