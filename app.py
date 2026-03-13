import streamlit as st
import pandas as pd
import joblib
import json
import matplotlib.pyplot as plt
import plotly.express as px

# Load model and metrics
model = joblib.load("model.pkl")
with open("metrics.json") as f:
    metrics = json.load(f)

st.set_page_config(page_title="AI Health Analyzer", layout="centered")

st.title("🧠 AI Health Analyzer")

# User inputs
st.sidebar.header("Enter your details")
age = st.sidebar.number_input("Age", min_value=1, max_value=120, value=25)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
height = st.sidebar.number_input("Height (meters)", min_value=0.5, max_value=2.5, value=1.75, step=0.01)
weight = st.sidebar.number_input("Weight (kg)", min_value=10, max_value=300, value=70, step=0.1)

if st.sidebar.button("Analyze"):
    # Prepare input
    gender_val = 1 if gender=="Male" else 0
    input_data = [[age, gender_val, height, weight]]

    # Prediction
    pred = model.predict(input_data)[0]
    prob = max(model.predict_proba(input_data)[0])
    bmi = round(weight/(height*height),2)

    # Show results
    st.subheader("📊 Prediction Results")
    st.write(f"**BMI:** {bmi}")
    st.write(f"**Prediction:** {pred}")
    st.write(f"**Confidence:** {prob:.2f}")

    # Accuracy
    st.subheader("🏆 Model Accuracy")
    st.write(f"{metrics['accuracy']*100:.2f} %")

    # Feature importance chart
    st.subheader("🔍 Feature Importance")
    features = metrics["feature_importance"]
    fig = px.bar(
        x=list(features.keys()),
        y=list(features.values()),
        labels={"x":"Feature", "y":"Importance"},
        text=list(features.values())
    )
    st.plotly_chart(fig)

    # Confusion matrix
    st.subheader("📉 Confusion Matrix")
    cm = pd.DataFrame(metrics["confusion"])
    st.dataframe(cm) 