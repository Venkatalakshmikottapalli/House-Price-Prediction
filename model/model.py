# Import the libraries
import os
import joblib
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
import xgboost as xgb
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Load data function
def load_data(filepath):
    return pd.read_csv(filepath)

# Load model function
def load_model(model_path):
    return joblib.load(model_path)

# Train model function
def train_model(X, y, params=None, random_state=42):
    if params:
        model = xgb.XGBRegressor(**params, random_state=random_state)
    else:
        model = xgb.XGBRegressor(random_state=random_state)
    model.fit(X, y)
    return model

# Test model function
def test_model(X, y, model):
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y, y_pred)
    
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"Root Mean Squared Error: {rmse:.2f}")
    print(f"R²: {r2:.3f}")
    
    return mse, rmse, r2

# Save model function
def save_model(model, filename, dirpath=''):
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)
    joblib.dump(model, f"{dirpath}/{filename}")

# Plotting function (optional)
def plot_feature_importance(model, X):
    xgb.plot_importance(model, importance_type='weight', max_num_features=10)
    plt.title('Feature Importance')
    plt.show()

if __name__ == "__main__":
    # Load data
    data = load_data("https://raw.githubusercontent.com/Venkatalakshmikottapalli/House-Price-Prediction/refs/heads/main/data/processed/house_price_prediction.csv") 

    # Prepare train and test data
    X = data.drop('price', axis=1)  
    y = data['price']  
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model with the best hyperparameters
    best_params = {
        'learning_rate': 0.1,
        'max_depth': 7,
        'n_estimators': 100,
        'subsample': 1.0,
        'colsample_bytree': 0.8
    }
    model = train_model(X_train, y_train, best_params, random_state=42)

    # Test the model
    mse, rmse, r2 = test_model(X_test, y_test, model)
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"Root Mean Squared Error: {rmse:.2f}")
    print(f"R²: {r2:.3f}")

    # Plot feature importance (optional)
    plot_feature_importance(model, X)

    # Save the trained model 
    model_path = os.path.join(os.path.dirname(__file__), 'xgb_regressor_model.pkl')
    joblib.dump(model, model_path, compress=3)
    print(f"Model saved to {model_path}")
