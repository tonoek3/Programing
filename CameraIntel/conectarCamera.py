import pyrealsense2 as rs
import numpy as np
import cv2

pipe = rs.pipeline()
cfg = rs.config()

cfg.enable_stream(rs.stream.color, 640,480, rs.format.bgr8, 40)
cfg.enable_stream(rs.stream.depth, 640,480, rs.format.z16, 40)

pipe.start(cfg)

while True:
    frame = pipe.wait_for_frames()
    depth_frame = frame.get_depth_frame()
    color_frame = frame.get_color_frame()

    depth_image = np.asanyarray(depth_frame.get_data)
    color_image = np.asanyarray(color_frame.get_data)

    cv2.imshow("rgb", color_image)
    cv2.imshow("depth", depth_image)





