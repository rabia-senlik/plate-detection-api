
# main.py
from fastapi import FastAPI, File, UploadFile
from model.plate_model import predict_plate

app = FastAPI()

@app.post("/predict-image")
async def predict_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    results = predict_plate(image_bytes)
    return {"detections": results}
