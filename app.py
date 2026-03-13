import streamlit as st
import pandas as pd
import joblib
import json
import plotly.express as px
import requests

# -----------------------------
# Load ML model and metrics
# -----------------------------
model = joblib.load("model.pkl")
with open("metrics.json") as f:
    metrics = json.load(f)

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(page_title="AI Health Analyzer", layout="wide")
st.title("🧠 AI Health Analyzer")

# -----------------------------
# Sidebar inputs for health analysis
# -----------------------------
st.sidebar.header("Enter your details")
age = st.sidebar.number_input("Age", min_value=1, max_value=120, value=25, step=1)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
height = st.sidebar.number_input("Height (meters)", min_value=0.5, max_value=2.5, value=1.75, step=0.01)
weight = st.sidebar.number_input("Weight (kg)", min_value=10.0, max_value=300.0, value=70.0, step=0.1)

if st.sidebar.button("Analyze"):
    # Prepare input for ML model
    gender_val = 1 if gender == "Male" else 0
    input_data = [[age, gender_val, height, weight]]

    prediction = model.predict(input_data)[0]
    probability = max(model.predict_proba(input_data)[0])
    bmi = round(weight / (height * height), 2)

    # -----------------------------
    # Display Prediction Results
    # -----------------------------
    st.subheader("📊 Prediction Results")
    st.write(f"**BMI:** {bmi}")
    st.write(f"**Prediction:** {prediction}")
    st.write(f"**Confidence:** {probability:.2f}")

    # Model Accuracy
    st.subheader("🏆 Model Accuracy")
    st.write(f"{metrics['accuracy']*100:.2f} %")

    # Feature Importance
    st.subheader("🔍 Feature Importance")
    features = metrics["feature_importance"]
    fig = px.bar(
        x=list(features.keys()),
        y=list(features.values()),
        labels={"x":"Feature", "y":"Importance"},
        text=[f"{v:.2f}" for v in features.values()],
        title="Feature Importance"
    )
    st.plotly_chart(fig)

    # Confusion Matrix
    st.subheader("📉 Confusion Matrix")
    cm = pd.DataFrame(metrics["confusion"])
    st.dataframe(cm)

# -----------------------------
# Chatbot section in sidebar
# -----------------------------
st.sidebar.header("💬 Health Chatbot")
user_message = st.sidebar.text_input("Ask a question...")

if st.sidebar.button("Send") and user_message.strip() != "":
    try:
        # Replace this URL with your n8n webhook URL
        webhook_url = "https://ljv8502d6t.app.n8n.cloud/webhook/bf0bef5c-a54b-448e-8658-e46bfe31bf90/chat"

        # Send user message to n8n
        response = requests.post(webhook_url, json={"message": user_message})
        if response.status_code == 200:
            bot_reply = response.json().get("reply", "🤖 Bot did not respond.")
        else:
            bot_reply = "❌ Failed to get response from chatbot."
    except Exception as e:
        bot_reply = f"❌ Error: {str(e)}"

    st.sidebar.markdown(f"**You:** {user_message}")
    st.sidebar.markdown(f"**Bot:** {bot_reply}")