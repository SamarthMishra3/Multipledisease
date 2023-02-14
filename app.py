import streamlit as st
import pandas as pd
import numpy as np
import pickle
from streamlit_option_menu import option_menu
import sklearn
import base64
from sklearn.preprocessing import StandardScaler


scaler = StandardScaler()
d_model= pickle.load(open('diabetee.pkl', 'rb'))
h_model= pickle.load(open('heart.pkl', 'rb'))
def d_prediction(A,B,C,D,E,F,G,H):
    ipd = (A,B,C,D,E,F,G,H)
    #print(ipd)
    ipd_as_na = np.asarray(ipd)
    std = ipd_as_na.reshape(1, -1)
    #print(std)
    #std_data = scaler.fit_transform(std)
    #print(std_data)
    pred = d_model.predict(std)
    return pred

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()} );
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

with st.sidebar:

    selected = option_menu('Multiple Disease Prediction System' ,
                           ['Diabetes Prediction' , 'Heart Disease Prediction'],
                           icons=['activity' , 'heart'],
                           default_index = 0)

if (selected == 'Diabetes Prediction' ):

    add_bg_from_local("diabetess.png")


    st.title("Diabetes Prediction using ML" )

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value(systolic)')

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

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):
        diab_prediction = d_prediction(
            Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)

        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)


if(selected =='Heart Disease Prediction'):

    add_bg_from_local("Heartt.png")
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('Thalassemia:' , '0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        heart_prediction = h_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
