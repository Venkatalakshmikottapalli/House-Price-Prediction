import os
import joblib
from flask import Flask, request, jsonify
import numpy as np

# Set up Flask app
app = Flask(__name__)

# Load the trained model
try:
    model_path = os.path.join(os.path.dirname(__file__), '../model/xgb_regressor_model.pkl')  
    model = joblib.load(model_path)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading the model: {str(e)}")
    model = None

# Route for health check
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "House Price Prediction API is running."})

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded.'}), 500

    try:
        # Parse JSON input
        data = request.json
        
        # Ensure all required fields are present
        required_features = [
            'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
            'waterfront', 'view', 'condition', 'sqft_above', 'sqft_basement',
            'yr_built', 'yr_renovated', 'city_encoded', 'zip_encoded'
        ]
        
        # Check if all required features are in the input data
        if not all(feature in data for feature in required_features):
            return jsonify({'error': 'Missing required features'}), 400
        
        # Prepare input data in the correct format for prediction
        input_data = [
            int(data['bedrooms']),
            int(data['bathrooms']),
            int(data['sqft_living']),
            int(data['sqft_lot']),
            int(data['floors']),
            int(data['waterfront']),
            int(data['view']),
            int(data['condition']),
            int(data['sqft_above']),
            int(data['sqft_basement']),
            int(data['yr_built']),
            int(data['yr_renovated']),
            int(data['city_encoded']),
            int(data['zip_encoded'])
        ]

        # Make prediction
        prediction = model.predict([input_data])[0]

        # Convert NumPy float32 to Python float
        prediction = float(prediction)

        # Return prediction result
        return jsonify({
            'predicted_price': round(prediction, 2)
        })
        
    except KeyError as e:
        return jsonify({'error': f'Missing key: {str(e)}'}), 400
    except ValueError as e:
        return jsonify({'error': f'Invalid input: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for health check
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'OK'}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
