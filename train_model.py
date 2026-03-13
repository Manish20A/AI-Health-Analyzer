import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import json

# Load dataset
df = pd.read_csv("ObesityDataSet_raw_and_data_sinthetic.csv")

# Encode gender
le = LabelEncoder()
df["Gender"] = le.fit_transform(df["Gender"])

# Features and target
X = df[["Age","Gender","Height","Weight"]]
y = df["NObeyesdad"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=200)
model.fit(X_train, y_train)

# Predictions
pred = model.predict(X_test)

# Accuracy, feature importance, confusion matrix
accuracy = accuracy_score(y_test, pred)
cm = confusion_matrix(y_test, pred).tolist()
report = classification_report(y_test, pred, output_dict=True)
importance = dict(zip(X.columns, model.feature_importances_))

# Save model and metrics
joblib.dump(model, "model.pkl")
metrics = {
    "accuracy": accuracy,
    "confusion": cm,
    "classification_report": report,
    "feature_importance": importance
}
with open("metrics.json", "w") as f:
    json.dump(metrics, f)

print("Model trained successfully. Accuracy:", accuracy)