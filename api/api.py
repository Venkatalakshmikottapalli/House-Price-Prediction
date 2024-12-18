# Import required libraries
import os
import joblib
from flask import Flask, request, jsonify

# Set up Flask app
app = Flask(__name__)

# Load the trained model
try:
    model_path = os.path.join(os.path.dirname(__file__), '../model/xgb_model.pkl')
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
        
        # Extract input features
        input_data = [
            float(data['bedrooms']),
            float(data['bathrooms']),
            float(data['sqft_living']),
            float(data['sqft_lot']),
            float(data['floors']),
            int(data['waterfront']),
            int(data['view']),
            int(data['condition']),
            float(data['sqft_above']),
            float(data['sqft_basement']),
            int(data['yr_built']),
            int(data['yr_renovated']),
            int(data['zip_encoded'])
        ]

        # Make prediction
        prediction = model.predict([input_data])[0]
        
        # Round prediction to nearest integer 
        rounded_prediction = round(prediction)

        # Return prediction result
        return jsonify({
            'predicted_price': rounded_prediction
        })

    except KeyError as e:
        return jsonify({'error': f'Missing key: {str(e)}'}), 400
    except ValueError as e:
        return jsonify({'error': f'Invalid input: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
