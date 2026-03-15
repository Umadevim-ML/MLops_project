import streamlit as st
import requests
import os

st.title("AI Salary Predictor")

age = st.slider("Age",18,60)
experience = st.slider("Years of Experience",0,20)
education = st.selectbox("Education Level",
["Bachelor","Master","PhD"])

edu_map = {
"Bachelor":1,
"Master":2,
"PhD":3
}

if st.button("Predict Salary"):

    url = "http://127.0.0.1:8000/predict"

    data = {
        "age":age,
        "experience":experience,
        "education":edu_map[education]
    }

    res = requests.post(url,json=data)

    salary = res.json()["predicted_salary"]

    st.success(f"Predicted Salary : ${salary:,.2f}")