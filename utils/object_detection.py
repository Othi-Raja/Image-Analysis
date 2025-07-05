# utils/object_detection.py
from ultralytics import YOLO
model = YOLO("yolov8n.pt")  # download once
def detect_objects(image_path):
    results = model(image_path)
    classes = results[0].names
    detections = results[0].boxes.cls.cpu().tolist()
    detected = [classes[int(i)] for i in detections]
    return list(set(detected))
