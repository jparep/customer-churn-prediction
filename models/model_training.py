import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib
from models.preprocessing import load_data, preprocess_data  # Import preprocessing functions

# Load raw data
raw_data_path = "data/raw/telco_customer_churn.csv"
raw_data = load_data(raw_data_path)

# Preprocess the data
X, y, preprocessor = preprocess_data(raw_data)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(classification_report(y_test, y_pred))

# Save the trained model and preprocessor
with open("models/churn_model.jobil", "wb") as model_file:
    joblib.dump(model, model_file)

with open("models/preprocessor.jobil", "wb") as preprocessor_file:
    joblib.dump(preprocessor, preprocessor_file)

print("Model and preprocessor saved!")
