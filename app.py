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
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1)
    with col2:
        Glucose = st.number_input('Glucose Level', min_value=0.0)
    with col3:
        BloodPressure = st.number_input('Blood Pressure value', min_value=0.0)
    with col1:
        SkinThickness = st.number_input('Skin Thickness value', min_value=0.0)
    with col2:
        Insulin = st.number_input('Insulin Level', min_value=0.0)
    with col3:
        BMI_value = st.number_input('BMI value', min_value=0.0)
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0, format="%.3f")
    with col2:
        Age = st.number_input('Age of the Person', min_value=0, step=1)


    # for prediction

    #predict button is clicked
    if st.button('Diabetes Test Result'):
        # collect raw inputs 
        inputs = [ Pregnancies, Glucose, BloodPressure,
                   SkinThickness, Insulin, BMI_value,
                     DiabetesPedigreeFunction, Age ]
        
        # Scale the inputs
        inputs_scaled = diabetes_scaler.transform([inputs])
        # Make prediction
        diabetes_prediction = diabetes_model.predict(inputs_scaled)
        
        if (diabetes_prediction[0] == 1):
            st.error('The person is diabetic')
        else:
            st.success('The person is not diabetic')

#------------------------------------------------------

#Heart Disease Prediction page

if (selected =='Heart Disease Prediction'):

    st.title('Heart Disease Prediction using ML')

    #getting the input data from the user
    #columns for input fields

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age of the Person', min_value=0, step=1)
    with col2:
        sex = st.selectbox('Sex of the Person', options=[0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male')
    with col3:
        cp = st.selectbox('Chest Pain types', options=[0, 1, 2, 3], 
                          format_func=lambda x: ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'][x])
    with col1:
        trestbps = st.number_input('Resting Blood Pressure value', min_value=0.0)
    with col2:      
        chol = st.number_input('Serum Cholestoral in mg/dl', min_value=0.0)
    with col3:  
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=[0, 1], format_func=lambda x: 'False' if x == 0 else 'True')
    with col1:
        restecg = st.selectbox('Resting Electrocardiographic results', options=[0, 1, 2],
                               format_func=lambda x: ['Normal', 'ST-T wave abnormality', 'Left ventricular hypertrophy'][x])
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved', min_value=0.0)     
    with col3: 
        exang = st.selectbox('Exercise Induced Angina', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise relative to rest', min_value=0.0)
    with col2:
        slope = st.selectbox('Slope of the peak exercise ST segment', options=[0, 1, 2],
                             format_func=lambda x: ['Upsloping', 'Flat', 'Downsloping'][x])
    with col3:
        ca = st.selectbox('Number of major vessels colored by fluoroscopy', options=[0, 1, 2, 3])
    with col1:
        thal = st.selectbox('Thalassemia', options=[1, 2, 3],
                            format_func=lambda x: {1: 'Normal', 2: 'Fixed Defect', 3: 'Reversible Defect'}[x])
    
    # for prediction

    #predict button is clicked
    if st.button('Heart Disease Test Result'):

        #collect raw inputs
        inputs = [age, sex, cp, trestbps, chol, fbs, restecg,
                   thalach, exang, oldpeak, slope, ca, thal]

        # Scale the inputs
        inputs_scaled = heart_scaler.transform([inputs])
        # Make prediction
        heart_prediction = heart_model.predict(inputs_scaled)
        
        if (heart_prediction[0] == 1):
            st.error('The person has heart disease')
        else:
            st.success('The person does not have heart disease')