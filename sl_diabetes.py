import pickle
import streamlit as st

#load model
db_model = pickle.load(open('diabetes_model.sav','rb'))


st.title('Aplikasi Prediksi Diabetes')

col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.text_input('Input nilai pregnancies')

with col2:
    Glucose = st.text_input('Input nilai glucose')

with col1:
    BloodPressure = st.text_input('Input nilai blood presure')

with col2:
    SkinThickness = st.text_input('Input nilai skin thickness')

with col1:
    Insulin = st.text_input('Input nilai insulin')

with col2:
    BMI = st.text_input('Input nilai BMI')

with col1:
    DiabetesPedigreeFunction = st.text_input('Input nilai diabetes pedigree function')

with col2:
    Age = st.text_input('Input nilai age')

diab_diagnosis =''

if st.button ('Test Prediksi Diabetes') :
    diab_prediction = db_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(diab_prediction[0]==1):
        diab_diagnosis = 'Pasien terkena diabetes'
    else:
        diab_diagnosis = 'Pasien tidak terkena diabetes'
    st.success(diab_diagnosis)