# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 17:29:15 2026

@author: thisa
"""

from os import name
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load custom CSS
def load_css():
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Apply custom styling
load_css()

# Load models and scalers
# Load models and scalers
with open('models/diabetes_model.pkl', 'rb') as f:
    diabetes_model = pickle.load(f)

with open('models/diabetes_scaler.pkl', 'rb') as f:
    diabetes_scaler = pickle.load(f)

with open('models/heart_model.pkl', 'rb') as f:
    heart_model = pickle.load(f)

with open('models/heart_scaler.pkl', 'rb') as f:
    heart_scaler = pickle.load(f)
    
# sidebar for navigate

with st.sidebar: selected = option_menu( 'Multiple Disease Prediction System', 
                                        ['Diabetes Prediction',
                                         'Heart Disease Prediction',],

                                        icons = ['activity','heart',],

                                        default_index=0 )

#------------------------------------------------------
#Diabetes Prediction page
if (selected =='Diabetes Prediction'):

    st.title('Diabetes Prediction using ML')

    #getting the input data from the user
    #columns for input fields

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI_value = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')


    # for prediction

    diabetes_diagnosis = ''

    #predict button is clicked
    if st.button('Diabetes Test Result'):
        # collect raw inputs 
        inputs = [ Pregnancies, Glucose, BloodPressure,
                   SkinThickness, Insulin, BMI_value,
                     DiabetesPedigreeFunction, Age ]
        try:
            # Convert to float
            inputs_float = [float(x) for x in inputs]
            # Scale the inputs
            inputs_scaled = diabetes_scaler.transform([inputs_float])
            # Make prediction
            diabetes_prediction = diabetes_model.predict(inputs_scaled)
            if (diabetes_prediction[0] == 1):
                diabetes_diagnosis = 'The person is diabetic'
            else:
                diabetes_diagnosis = 'The person is not diabetic'
        except ValueError:
            diabetes_diagnosis = 'Please enter valid input values'

    st.success(diabetes_diagnosis)

#------------------------------------------------------

#Heart Disease Prediction page

if (selected =='Heart Disease Prediction'):

    st.title('Heart Disease Prediction using ML')

    #getting the input data from the user
    #columns for input fields

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age of the Person')
    with col2:
        sex = st.text_input('Sex of the Person (0 = Female, 1 = Male)')
    with col3:
        cp = st.text_input('Chest Pain types (0-3)')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure value')
    with col2:      
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:  
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = True; 0 = False)')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results (0-2)')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')     
    with col3: 
        exang = st.text_input('Exercise Induced Angina (1 = Yes; 0 = No)')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise relative to rest')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment (0-2)')
    with col3:
        ca = st.text_input('Number of major vessels (0-3) colored by fluoroscopy')
    with col1:
        thal = st.text_input('Thalassemia (1 = Normal; 2 = Reversible Defect; 3 = Fixed Defect)')
    
    # for prediction
    heart_diagnosis = ''

    #predict button is clicked
    if st.button('Heart Disease Test Result'):

        #collect raw inputs
        inputs = [age, sex, cp, trestbps, chol, fbs, restecg,
                   thalach, exang, oldpeak, slope, ca, thal]

        try:
            # Convert to float
            inputs_float = [float(x) for x in inputs]
            # Scale the inputs
            inputs_scaled = heart_scaler.transform([inputs_float])
            # Make prediction
            heart_prediction = heart_model.predict(inputs_scaled)
            if (heart_prediction[0] == 1):
                heart_diagnosis = 'The person has heart disease'
            else:
                heart_diagnosis = 'The person does not have heart disease'
        except ValueError:
            heart_diagnosis = 'Please enter valid input values'

    st.success(heart_diagnosis)