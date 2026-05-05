from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

kmeans = joblib.load('models/kmeans_model.pkl')
scaler = joblib.load('models/scaler.pkl')
pca = joblib.load('models/pca.pkl')

app = FastAPI(title="Breast Cancer Clustering API")

class PatientData(BaseModel):
    features: list[float]  

@app.get("/")
def home():
    return {"message": "Breast Cancer Clustering API is running! 🎉"}

@app.post("/predict")
def predict(data: PatientData):
    if len(data.features) != 30:
        return {"error": f"Expected 30 features, got {len(data.features)}"}
    
    arr = np.array(data.features).reshape(1, -1)
    scaled = scaler.transform(arr)
    pca_transformed = pca.transform(scaled)
    cluster = kmeans.predict(pca_transformed)[0]
    
    label = "Malignant" if cluster == 0 else "Benign"
    
    return {
        "cluster": int(cluster),
        "prediction": label
    }