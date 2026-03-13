# AI Health Analyzer – Stakeholder Overview

## Project Summary
The **AI Health Analyzer** is a web application that predicts a user’s **obesity category** based on age, gender, height, and weight using a trained Machine Learning model. It also provides analytics such as BMI, prediction confidence, model accuracy, feature importance, and confusion matrix. A chatbot is integrated for additional health guidance.

---

## Key Features

- **AI Prediction**: Obesity category prediction (Normal, Overweight, Obesity, etc.)
- **Health Metrics**:
  - BMI calculation
  - Prediction confidence score
- **Model Analytics**:
  - Accuracy percentage
  - Feature importance visualization
  - Confusion matrix table
- **Interactive Chatbot**: Users can ask health-related questions.
- **Dynamic Dashboard**: Results displayed only after user input to improve UX.

---

## Technical Overview

- **Frontend**: HTML, TailwindCSS, Chart.js, JavaScript
- **Backend**: Python Flask
- **Machine Learning**: Random Forest Classifier trained on obesity dataset
- **Data**: ~2100 records, including Age, Gender, Height, Weight, Lifestyle
- **Deployment**: Local or cloud-hosted Flask app

---

## Business Value

- Provides **quick health insights** for end users.
- Offers **data-driven visual analytics** for better understanding of risk factors.
- Can integrate with chatbots for **personalized health guidance**.
- Useful for **healthcare apps, gyms, or nutrition platforms** for engagement.

---

## Metrics & Performance

- **Model Accuracy**: 97.4%
- **Important Features**:
  - Weight: 0.555
  - Height: 0.208
  - Age: 0.141
  - Gender: 0.096
- **Prediction Confidence**: Varies per user input (0–1 scale)
- **Confusion Matrix**: Detailed classification evaluation

---

## Next Steps / Recommendations

- Deploy on cloud for scalable access.
- Enhance ML explainability using SHAP or LIME.
- Add historical tracking for users to monitor changes.
- Integrate more lifestyle factors (e.g., diet, exercise, sleep) for better accuracy.
- Improve chatbot capabilities with personalized recommendations.
