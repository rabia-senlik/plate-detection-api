
# 🚗 License Plate Detection API

This project presents an object detection system trained using the YOLOv8 model as a web service with FastAPI. It detects vehicle license plates in uploaded images and returns bounding box (box) information.

## 📸 Example Usage

When you send an image to the API, you will receive an output in JSON format like this:

```json
{
  "detections": [
    {
      "bbox": [123, 456, 234, 567],
      "score": 0.87,
      "class": "license_plate"
    }
  ]
}
```

---

## 🔧 Installation

You can run the project on your local machine by following the steps below:

### 1. Clone the Repository and Set Up the Environment

```bash
git clone https://github.com/rabia-senlik/plate-detection-api.git
cd plate-detection-api
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Add the Model File

Replace the `training/best.pt` file with your own trained YOLOv8 model file. Check the model path in `model/plate_model.py`.

### 3. Start the API

```bash
uvicorn main:app --reload --port 8002
```

### 4. Test with Swagger UI

Visit [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs) in your browser to upload images and test the API.

---

## 🧠 Technologies Used

- Python  
- FastAPI  
- Ultralytics YOLOv8  
- OpenCV  
- Pillow (PIL)

---

## 💡 Development Plans

- Drawing the detected license plates on the image  
- Reading the license plate text with OCR  
- Frontend interface integration

---

## 👤 Developer

- **Name:** Rabia Şenlik  
- **GitHub:** [@rabia-senlik](https://github.com/rabia-senlik)
