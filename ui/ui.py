import streamlit as st
import requests

# Set the title of the app
st.set_page_config(page_title="House Price Prediction", page_icon="🏠", layout="centered")

# Streamlit App Title
st.title("🏠 House Price Prediction App")
st.markdown("Enter the details of the house below to predict its price.")

# Sidebar for user input
st.sidebar.header("Input Features")
st.sidebar.markdown("Please provide the following details:")

# Input fields for features
bedrooms = st.sidebar.number_input("Number of Bedrooms", min_value=0, max_value=10, value=3)
bathrooms = st.sidebar.number_input("Number of Bathrooms", min_value=0, max_value=10, value=2)
sqft_living = st.sidebar.number_input("Living Area (sqft)", min_value=0, max_value=10000, value=2000)
sqft_lot = st.sidebar.number_input("Lot Size (sqft)", min_value=0, max_value=100000, value=5000)
floors = st.sidebar.number_input("Number of Floors", min_value=1, max_value=4, value=1)
waterfront = st.sidebar.selectbox("Waterfront (0 = No, 1 = Yes)", [0, 1])
view = st.sidebar.number_input("View Rating (0-4)", min_value=0, max_value=4, value=0)
condition = st.sidebar.number_input("Condition (1-5)", min_value=1, max_value=5, value=3)
sqft_above = st.sidebar.number_input("Above Ground Area (sqft)", min_value=0, max_value=10000, value=1500)
sqft_basement = st.sidebar.number_input("Basement Area (sqft)", min_value=0, max_value=5000, value=500)
yr_built = st.sidebar.number_input("Year Built", min_value=1800, max_value=2023, value=2000)
yr_renovated = st.sidebar.number_input("Year Renovated (0 if never)", min_value=0, max_value=2023, value=0)
city_encoded = st.sidebar.number_input("City Code", min_value=0, max_value=100, value=1)
zip_encoded = st.sidebar.number_input("Zip Code (Encoded)", min_value=0, max_value=99999, value=98101)

# API URL
api_url = "http://127.0.0.1:5000/predict"  # Replace with your API endpoint

# Predict button
if st.button("Predict House Price"):
    # Prepare the data payload
    data = {
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "sqft_living": sqft_living,
        "sqft_lot": sqft_lot,
        "floors": floors,
        "waterfront": waterfront,
        "view": view,
        "condition": condition,
        "sqft_above": sqft_above,
        "sqft_basement": sqft_basement,
        "yr_built": yr_built,
        "yr_renovated": yr_renovated,
        "city_encoded": city_encoded,
        "zip_encoded": zip_encoded,
    }

    try:
        # Call the API
        response = requests.post(api_url, json=data)

        # Check the response status
        if response.status_code == 200:
            result = response.json()
            predicted_price = result.get("predicted_price", "N/A")
            st.success(f"🏡 The predicted house price is **${predicted_price:,.2f}**")
        else:
            st.error(f"Error: {response.json().get('error', 'Unknown error')}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Footer
st.markdown("---")
st.markdown(
    "💡 *This app uses a machine learning model to predict house prices based on various input features.*"
)