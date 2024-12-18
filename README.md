
# House Price Prediction

This project predicts the price of houses based on various features using machine learning models. The system allows users to input details about a house (such as the number of bedrooms, bathrooms, square footage, etc.) and predicts the house price.

## Project Structure

```
HOUSE-PRICE-PREDICTION/
├── api/
│   └── api.py             # API implementation for the prediction model
├── data/
│   └── [dataset files]    # Data files used for model training and testing
├── model/
│   ├── model.py           # Model training and evaluation code
│   └── xgb_model.pkl      # Saved trained model (XGBoost)
├── notebooks/
│   ├── V_Kottaplli_data_preprocessing.ipynb  # Data preprocessing notebook
│   ├── V_Kottaplli_Model_building.ipynb      # Model building notebook
├── ui/
│   └── ui.py              # Streamlit app for user interaction
├── LICENSE                # License file
├── README.md              # Project description and instructions
```

## Installation

To set up the environment and run this project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/house-price-prediction.git
   ```

2. **Install dependencies:**  
   Ensure you have Python installed, and then install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

   If a `requirements.txt` file is not available, install necessary libraries manually:
   ```bash
   pip install streamlit xgboost scikit-learn pandas numpy requests
   ```

3. **Run the Streamlit UI:**  
   Once the environment is set up, you can start the UI:
   ```bash
   streamlit run ui/ui.py
   ```

4. **API:**  
   If you want to test or deploy the model via an API, run the `api/api.py` script to start a Flask-based API.

## Features

- **House Price Prediction:** Predict the price of a house by providing key details such as the number of bedrooms, bathrooms, square footage, etc.
- **Interactive UI:** A simple, user-friendly interface built using Streamlit for easy input and prediction results.

## Model Details

The project uses an XGBoost model trained on house pricing data. The model is saved in the `model/xgb_model.pkl` file, which can be loaded and used to make predictions.

### Key Factors Affecting Prediction:
- Square footage of the living area
- Zip code of the property
- Square footage of the lot
- Year the property was built

## How to Use

Enter the details of the house you want to predict the price for, such as:
- Number of bedrooms
- Number of bathrooms
- Square footage of the living area
- Zip code
- Year built

Click the "Predict House Price" button to receive an estimated house price.

## Contributing

If you would like to contribute to this project, please fork the repository and create a pull request with your proposed changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Created by

Venkatalakshmi Kottapalli, Yeshiva University
