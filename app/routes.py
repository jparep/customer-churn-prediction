from flask import Blueprint, request, jsonify
import pickle
import pandas as pd

# Create Blueprint for API routes
api = Blueprint('api', __name__)

# Load trained model
with open("models/churn_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

@api.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data
        data = request.get_json()
        input_features = pd.DataFrame([data])

        # Predict using the model
        prediction = model.predict(input_features)

        return jsonify({"churn": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 400