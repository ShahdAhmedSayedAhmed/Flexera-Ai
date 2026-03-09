# import os
# import uvicorn

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 8000))
#     uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=False)
from fastapi import FastAPI
from ultralytics import YOLO
import cv2
import numpy as np

app = FastAPI()

# Example YOLO model
model = YOLO("yolov8n.pt")  # lightweight model

@app.get("/")
def home():
    return {"message": "YOLO Ready on Railway!"}

@app.post("/detect/")
def detect_image(image_path: str):
    # اقرأ الصورة بدون GUI
    img = cv2.imread(image_path)
    if img is None:
        return {"error": "Image not found"}

    # Resize للتأكد من توافق النموذج
    img = cv2.resize(img, (640, 640))

    # استخدم YOLO للـ detection
    results = model(img)

    # تحويل النتائج summary فقط
    summary = results[0].boxes.xyxy.tolist()  # قائمة الصناديق
    return {"detections": summary}