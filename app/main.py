import os
import io
import json
import numpy as np
import tensorflow as tf
from PIL import Image
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Plant Disease Prediction API")

# CORS (required for frontend JS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "trained model", "plant_disease_prediction_model.h5")
CLASS_INDEX_PATH = os.path.join(BASE_DIR, "class_indices.json")

# Load model and class indices
model = tf.keras.models.load_model(MODEL_PATH)
class_indices = json.load(open(CLASS_INDEX_PATH))

def load_and_preprocess_image(image: Image.Image, target_size=(224, 224)):
    image = image.resize(target_size)
    image = np.array(image)
    image = np.expand_dims(image, axis=0)
    image = image.astype("float32") / 255.0
    return image

# Serve index.html at root
@app.get("/")
async def root():
    return FileResponse(os.path.join(BASE_DIR, "index.html"))

# Serve static files (CSS and JS) from frontend folder
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "frontend")), name="static")

# Prediction endpoint
@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    contents = await image.read()
    img = Image.open(io.BytesIO(contents)).convert("RGB")

    preprocessed_img = load_and_preprocess_image(img)
    predictions = model.predict(preprocessed_img)

    predicted_class_index = int(np.argmax(predictions, axis=1)[0])
    predicted_class_name = class_indices[str(predicted_class_index)]
    confidence = float(np.max(predictions))

    return {
        "prediction": predicted_class_name,
        "confidence": round(confidence * 100, 2)
    }