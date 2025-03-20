from ultralytics import YOLO

model = YOLO("results/weights/best.pt")
results = model("dataset/test/images/Cars96.png", save=True)
results[0].show()