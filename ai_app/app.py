from flask import Flask, request, render_template, jsonify
import joblib
import json

app = Flask(__name__)

# Load ML model and metrics
model = joblib.load("model.pkl")
with open("metrics.json") as f:
    metrics = json.load(f)

# Serve HTML page
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Prediction API for AJAX
@app.route("/predict", methods=["POST"])
def predict():
    age = float(request.form["age"])
    gender = request.form["gender"]
    height = float(request.form["height"])
    weight = float(request.form["weight"])

    gender_val = 1 if gender == "Male" else 0
    bmi = round(weight / (height * height), 2)

    input_data = [[age, gender_val, height, weight]]
    prediction = model.predict(input_data)
    probs = model.predict_proba(input_data)

    result = prediction[0]
    probability = float(max(probs[0]))

    response = {
        "bmi": bmi,
        "result": result,
        "probability": probability,
        "accuracy": round(metrics["accuracy"]*100,2),
        "features": metrics["feature_importance"],
        "confusion": metrics["confusion_matrix"]
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)