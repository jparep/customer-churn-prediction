from flask import Blueprint, request, jsonify
import joblib
import pandas as pd

# Create Blueprint for API routes
api = Blueprint('api', __name__)

# Load trained model
def load_model():
    try:
        return joblib.load("models/churn_model.joblib")
    except Exception as e:
        raise RuntimeError(f"Error loading model: {e}")

model = load_model()

@api.route('/predict', methods=['POST'])
def predict():
    """
    Predicts customer churn based on input features.
    Expects JSON input in the format:
    {
        "feature1": value1,
        "feature2": value2,
        ...
    }
    """
    try:
        # Validate input
        data = request.get_json()
        if not isinstance(data, dict):
            return jsonify({"error": "Invalid input format. Expecting a JSON object."}), 400
        
        # Convert input to DataFrame
        input_features = pd.DataFrame([data])
        
        # Make prediction
        prediction = model.predict(input_features)
        
        return jsonify({"churn": int(prediction[0])})
    except ValueError as ve:
        return jsonify({"error": f"Invalid input data: {ve}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
