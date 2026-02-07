# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 17:29:15 2026

@author: thisa
"""

from os import name
import pickle
import streamlit as st
from streamlit_option_menu import option_menu



# Load models
with open('C:/Users/thisa/OneDrive/Desktop/multiple_disease_prediction_system/saved_models/Diabetes_trained_model.sav', 'rb') as f:
    diabetes_model = pickle.load(f)

with open('C:/Users/thisa/OneDrive/Desktop/multiple_disease_prediction_system/saved_models/Heart_disease_trained_model.sav', 'rb') as f:
    heart_model = pickle.load(f)

with open('C:/Users/thisa/OneDrive/Desktop/multiple_disease_prediction_system/saved_models/Parkinson_disease_trained_model.sav', 'rb') as f:
    parkinson_model = pickle.load(f)


# sidebar for navigate

with st.sidebar: selected = option_menu( 'Multiple Disease Prediction System', 
                                        ['Diabetes Prediction',
                                         'Heart Disease Prediction',
                                         'Parkinson Disease Prediction'],

                                        icons = ['activity','heart','person'],

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
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')


    # for prediction

    diabetes_diagnosis = ''

    #predict button is clicked
    if st.button('Diabetes Test Result'):
        diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diabetes_prediction[0] == 1):
            diabetes_diagnosis = 'The person have diabetic'
        else:
            diabetes_diagnosis = 'The person does not have diabetic'

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
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person have heart disease'
        else:
            heart_diagnosis = 'The person does not have heart disease'
    st.success(heart_diagnosis)


#------------------------------------------------------

#Parkinson Disease Prediction page

if (selected =='Parkinson Disease Prediction'):

    st.title('Parkinson Disease Prediction using ML')

    #getting the input data from the user
    #columns for input fields

    col1, col2, col3 = st.columns(3)    

    with col1:
        mdvp = st.text_input('MDVP:Fo(Hz) - Average vocal fundamental frequency')
    with col2:
        mdvp_fhi = st.text_input('MDVP:Fhi(Hz) - Maximum vocal fundamental frequency')
    with col3:
        mdvp_flo = st.text_input('MDVP:Flo(Hz) - Minimum vocal fundamental frequency')
    with col1:
        mdvp_jitter = st.text_input('MDVP:Jitter(%) - Measure of variation in fundamental frequency')
    with col2:
        mdvp_jitter_abs = st.text_input('MDVP:Jitter(Abs) - Average absolute difference of fundamental frequency')
    with col3:
        mdvp_rap = st.text_input('MDVP:RAP - Relative amplitude perturbation')
    with col1:
        mdvp_ppq = st.text_input('MDVP:PPQ - 5-point period perturbation quotient')
    with col2:
        jitter_ddp = st.text_input('Jitter:DDP - Average absolute difference of fundamental frequency')
    with col3:
        mdvp_shimmer = st.text_input('MDVP:Shimmer - Measure of variation in amplitude')
    with col1:
        mdvp_shimmer_db = st.text_input('MDVP:Shimmer(dB) - Measure of variation in amplitude')  
    with col2:
        shimmer_apq3 = st.text_input('Shimmer:APQ3 - 3-point amplitude perturbation quotient')
    with col3:
        shimmer_apq5 = st.text_input('Shimmer:APQ5 - 5-point amplitude perturbation quotient')
    with col1:
        mdvp_apq = st.text_input('MDVP:APQ - 11-point amplitude perturbation quotient')
    with col2:
        shimmer_apq = st.text_input('Shimmer:APQ - 11-point amplitude perturbation quotient')
    with col3:
        nhr = st.text_input('NHR - Noise to Harmonics Ratio')
    with col1:
        hnr = st.text_input('HNR - Harmonics to Noise Ratio')
    with col2:
        rpde = st.text_input('RPDE - Recurrence Period Density Entropy')
    with col3:
        dfa = st.text_input('DFA - Detrended Fluctuation Analysis')
    with col1:
        spread1 = st.text_input('spread1 - Non-linear measure of fundamental frequency variation')  
    with col2:
        spread2 = st.text_input('spread2 - Non-linear measure of fundamental frequency variation')
    with col3:
        d2 = st.text_input('D2 - Correlation Dimension')
    with col1:
        ppe = st.text_input('PPE - Pitch Period Entropy')
    
    # for prediction
    parkinson_diagnosis = ''

    #predict button is clicked
    if st.button('Parkinson Disease Test Result'):      
        parkinson_prediction = parkinson_model.predict([[mdvp, mdvp_fhi, mdvp_flo, mdvp_jitter, mdvp_jitter_abs, mdvp_rap, mdvp_ppq, jitter_ddp, mdvp_shimmer, mdvp_shimmer_db, shimmer_apq3, shimmer_apq5, mdvp_apq, shimmer_apq, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]])
        if (parkinson_prediction[0] == 1):
            parkinson_diagnosis = 'The person have Parkinson disease'
        else:
            parkinson_diagnosis = 'The person does not have Parkinson disease'
    st.success(parkinson_diagnosis)
#------------------------------------------------------