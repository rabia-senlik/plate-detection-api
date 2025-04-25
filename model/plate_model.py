
# model/plate_model.py
from ultralytics import YOLO
import numpy as np
import cv2
from PIL import Image
import io

model = YOLO("best.pt")  # Eğittiğin model

def predict_plate(image_bytes):
    # Görseli oku ve OpenCV formatına çevir
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    # Tahmin yap
    results = model(img_cv)[0]
    detections = []

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
        if score > 0.5:
            detections.append({
                "bbox": [int(x1), int(y1), int(x2), int(y2)],
                "score": float(score),
                "class": results.names[int(class_id)]
            })

    return detections
