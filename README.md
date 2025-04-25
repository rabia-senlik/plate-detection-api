
# 🚗 Plaka Tespiti API (License Plate Detection API)

Bu proje, YOLOv8 modeli kullanılarak eğitilmiş bir nesne tespiti sistemini FastAPI ile web servisi olarak sunar. Yüklenen görsellerde araç plakalarını tespit eder ve bounding box (kutu) bilgileri ile birlikte döner.

## 📸 Örnek Kullanım

API'ye bir görsel gönderdiğinizde JSON formatında şu şekilde bir çıktı alırsınız:

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

## 🔧 Kurulum

Aşağıdaki adımlarla projeyi yerel bilgisayarınızda çalıştırabilirsiniz:

### 1. Depoyu Klonlayın ve Ortamı Hazırlayın

```bash
git clone https://github.com/rabia-senlik/plate-detection-api.git
cd plate-detection-api
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Model Dosyasını Ekleyin

`training/best.pt` dosyasını kendi eğittiğiniz YOLOv8 model dosyasıyla değiştirin. Model yolunu `model/plate_model.py` içinde kontrol edin.

### 3. API’yi Başlatın

```bash
uvicorn main:app --reload --port 8002
```

### 4. Swagger Arayüzü ile Test Edin

Tarayıcıdan [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs) adresine giderek görsel yükleyip test edebilirsiniz.

---

## 🧠 Kullanılan Teknolojiler

- Python  
- FastAPI  
- Ultralytics YOLOv8  
- OpenCV  
- Pillow (PIL)

---

## 💡 Geliştirme Planları

- Tespit edilen plakaların görüntü üzerine çizilmesi  
- OCR ile plaka metninin okunması  
- Frontend arayüzü entegrasyonu

---

## 👤 Geliştirici

- **İsim:** Rabia Şenlik  
- **GitHub:** [@rabia-senlik](https://github.com/rabia-senlik)
