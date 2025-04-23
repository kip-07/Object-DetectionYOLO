from ultralytics import YOLO
import cv2

model = YOLO('../yolo-weights/yolov8l.pt') #l large, n nano
results = model("Images/2.jpg", show=True)
cv2.waitKey(0) #to give delay in image

