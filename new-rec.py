import streamlit as st
import pandas as pd
import pickle


with open(r'C:\Users\LENOVO T480\Desktop\ㅤ\model.pkl', 'rb') as file:
    model = pickle.load(file)
st.write("place prediction")
cgpa = st.number_input("Enter your CGPA")
iq = st.number_input("Enter your IQ")

if st.button("Submit"):
    prediction = model.predict([[cgpa, iq]])
    if(prediction == 1):
        st.write("congrats man you got placed")
    else:
        st.write("sorry mate you didn't get placed")
