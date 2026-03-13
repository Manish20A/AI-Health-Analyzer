import pandas as pd
import joblib
import json

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load dataset
df = pd.read_csv("ObesityDataSet_raw_and_data_sinthetic.csv")

# Encode Gender
le = LabelEncoder()
df["Gender"] = le.fit_transform(df["Gender"])

# Features
X = df[["Age","Gender","Height","Weight"]]

# Target
y = df["NObeyesdad"]

# Split dataset
X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=200)
model.fit(X_train,y_train)

# Predictions
pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test,pred)

# Confusion matrix
cm = confusion_matrix(y_test,pred).tolist()

# Classification report
report = classification_report(y_test,pred,output_dict=True)

# Feature importance
importance = dict(zip(X.columns,model.feature_importances_))

# Save model
joblib.dump(model,"model.pkl")

# Save metrics
metrics = {
    "accuracy": accuracy,
    "confusion_matrix": cm,
    "classification_report": report,
    "feature_importance": importance
}

with open("metrics.json","w") as f:
    json.dump(metrics,f)

print("Model trained successfully")
print("Accuracy:", accuracy)