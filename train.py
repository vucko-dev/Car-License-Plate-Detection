from ultralytics import YOLO
import torch

model = YOLO("yolov8n.pt")  

# Train the model
results = model.train(
    data="/Users/srbislav98/Documents/carlicense/Car-License-Plate-Detection/dataset.yaml", 
    imgsz=640,
    epochs=20,
    batch=4, 
    workers=2,
    device="cpu"
)
