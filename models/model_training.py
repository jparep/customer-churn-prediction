import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# Load data from Snowflake or processed CSV
data = pd.read_csv("data/processed_data.csv")

# Preprocess data
X = data.drop(columns=['Churn', 'customerID'])
y = data['Churn']

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate and save model
accuracy = accuracy_score(y_test, model.predict(X_test))
print(f"Model Accuracy: {accuracy}")
pickle.dump(model, open("models/churn_model.pkl", "wb"))
