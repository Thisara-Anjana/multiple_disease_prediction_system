from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Models and Scalers
# Assuming models are in the parent directory's 'models' folder relative to this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, '..', 'models')

def load_model(filename):
    try:
        with open(os.path.join(MODELS_DIR, filename), 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        # Fallback for when running from root
        try:
             with open(os.path.join('models', filename), 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
             print(f"Error: Model file {filename} not found.")
             return None

diabetes_model = load_model('diabetes_model.pkl')
diabetes_scaler = load_model('diabetes_scaler.pkl')
heart_model = load_model('heart_model.pkl')
heart_scaler = load_model('heart_scaler.pkl')

# Pydantic Models for Input Validation
class DiabetesInput(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

class HeartInput(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: float
    chol: float
    fbs: int
    restecg: int
    thalach: float
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

@app.get("/")
def read_root():
    return {"message": "Disease Prediction API is running"}

@app.post("/predict/diabetes")
def predict_diabetes(data: DiabetesInput):
    if not diabetes_model or not diabetes_scaler:
        raise HTTPException(status_code=500, detail="Model or Scaler not loaded")
    
    input_data = [
        data.Pregnancies,
        data.Glucose,
        data.BloodPressure,
        data.SkinThickness,
        data.Insulin,
        data.BMI,
        data.DiabetesPedigreeFunction,
        data.Age
    ]
    
    # Scale and predict
    try:
        input_scaled = diabetes_scaler.transform([input_data])
        print(f"Diabetes Input: {input_data}")
        prediction = diabetes_model.predict(input_scaled)
        print(f"Diabetes Prediction: {prediction}")
        
        result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"
        return {"prediction": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict/heart")
def predict_heart(data: HeartInput):
    if not heart_model or not heart_scaler:
        raise HTTPException(status_code=500, detail="Model or Scaler not loaded")
    
    input_data = [
        data.age,
        data.sex,
        data.cp,
        data.trestbps,
        data.chol,
        data.fbs,
        data.restecg,
        data.thalach,
        data.exang,
        data.oldpeak,
        data.slope,
        data.ca,
        data.thal
    ]
    
    # Scale and predict
    try:
        input_scaled = heart_scaler.transform([input_data])
        print(f"Heart Input: {input_data}")
        prediction = heart_model.predict(input_scaled)
        print(f"Heart Prediction: {prediction}")
        
        result = "Heart Disease" if prediction[0] == 1 else "No Heart Disease"
        return {"prediction": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
