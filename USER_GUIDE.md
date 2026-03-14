# AI Health Analyzer – User Guide

## Welcome

The **AI Health Analyzer** is an interactive web application that helps you understand your obesity category, BMI, and health insights using AI.

---

## How to Use

1. Open the web app: `[http://127.0.0.1:5000](https://ai-health-analyzer-hn448rptzazhzrkpj5ozri.streamlit.app/#feature-importance)`
2. Fill in the input form:
   - **Age**: Enter your age in years.
   - **Gender**: Select Male or Female.
   - **Height**: Enter your height in meters (e.g., 1.75).
   - **Weight**: Enter your weight in kilograms (e.g., 70).
3. Click **Analyze**.

---

## What You Will See

After submitting, the app displays:

- **BMI**: Your Body Mass Index.
- **Prediction**: Your obesity category.
- **Confidence**: How confident the model is in the prediction.
- **Model Accuracy**: Overall model performance.
- **Feature Importance**: How much each input contributes to the prediction.
- **Confusion Matrix**: Model evaluation table.

> The results only appear **after submission**, ensuring a clean interface.

---

## Interactive Chatbot

- Click the **💬 button** at the bottom-right corner.
- Ask questions like:
  - “What can I do to maintain a healthy weight?”
  - “How can I reduce BMI?”
- The chatbot provides answers powered by the integrated n8n workflow.

---

## Tips for Best Results

- Enter accurate measurements for height and weight.
- Use the app in a well-lit environment for personal measurement checks.
- The predictions are **AI-based guidance**, not medical diagnosis.

---

## Support

For any issues:

- Ensure Flask server is running: `python app.py`
- Ensure `model.pkl` and `metrics.json` exist in the project folder.
- Contact your project admin for dataset updates or troubleshooting.
