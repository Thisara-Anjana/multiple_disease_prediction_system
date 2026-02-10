import gradio as gr
import pickle

# Load models
diabetes_model = pickle.load(open("saved_models/Diabetes_trained_model.sav", "rb"))
heart_model = pickle.load(open("saved_models/Heart_disease_trained_model.sav", "rb"))

def predict_diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness,
                     Insulin, BMI_value, DiabetesPedigreeFunction, Age):
    inputs = [Pregnancies, Glucose, BloodPressure, SkinThickness,
              Insulin, BMI_value, DiabetesPedigreeFunction, Age]
    prediction = diabetes_model.predict([inputs])[0]
    return "Diabetic" if prediction == 1 else "Not Diabetic"

def predict_heart(age, sex, cp, trestbps, chol, fbs, restecg,
                  thalach, exang, oldpeak, slope, ca, thal):
    inputs = [age, sex, cp, trestbps, chol, fbs, restecg,
              thalach, exang, oldpeak, slope, ca, thal]
    prediction = heart_model.predict([inputs])[0]
    return "Heart Disease" if prediction == 1 else "No Heart Disease"

diabetes_inputs = [gr.Number(label="Pregnancies"), gr.Number(label="Glucose"),
                   gr.Number(label="BloodPressure"), gr.Number(label="SkinThickness"),
                   gr.Number(label="Insulin"), gr.Number(label="BMI"),
                   gr.Number(label="DiabetesPedigreeFunction"), gr.Number(label="Age")]

heart_inputs = [gr.Number(label="Age"), gr.Number(label="Sex"),
                gr.Number(label="Chest Pain"), gr.Number(label="Resting BP"),
                gr.Number(label="Cholesterol"), gr.Number(label="Fasting Blood Sugar"),
                gr.Number(label="Rest ECG"), gr.Number(label="Max Heart Rate"),
                gr.Number(label="Exercise Angina"), gr.Number(label="Oldpeak"),
                gr.Number(label="Slope"), gr.Number(label="CA"), gr.Number(label="Thal")]

demo = gr.TabbedInterface([
    gr.Interface(fn=predict_diabetes, inputs=diabetes_inputs, outputs="text", title="Diabetes Prediction"),
    gr.Interface(fn=predict_heart, inputs=heart_inputs, outputs="text", title="Heart Disease Prediction")
], tab_names=["Diabetes", "Heart Disease"])

demo.launch()
