import streamlit as st
import requests

# Set the title of the app
st.set_page_config(page_title="Check Your Dream House Price", page_icon="🏠", layout="centered")

# Add a custom CSS style for the header and content
st.markdown("""
    <style>
    .main-heading {
        text-align: center;
        font-size: 2em;
        font-weight: bold;
        padding: 10px;
        margin-top: 0;
        background-color: white;
        position: sticky;
        top: 0;
        z-index: 100;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .content {
        padding-top: 10px; /* Minimal space after title */
    }
    </style>
""", unsafe_allow_html=True)

# Display a sticky header
st.markdown('<h1 class="main-heading">🏠 Check Your Dream House Price</h1>', unsafe_allow_html=True)

# Content section starts here
st.markdown('<div class="content"></div>', unsafe_allow_html=True)

# Sidebar with instructions about the house
st.sidebar.markdown("### 🏠 Check Your Dream House Price")
st.sidebar.markdown("""
    Everybody has a dream house! 🏡✨ Before making that big decision, why not predict the price of your ideal home?

This app lets you estimate the price of your dream house by entering details like location, size, number of rooms, and more. Simply provide the information, and our model will give you an estimate based on real estate data!

How to Use:

1. Fill in your house details.
                    
2. Click **"Predict"** for an estimate.
                    
3. Explore how different features affect the price.
                    
**Created by:**
**Venkatalakshmi Kottapalli, Yeshiva University**
                    
""")

# Input fields for the house features
bedrooms = st.text_input("Number of Bedrooms", placeholder="e.g., 3")
bathrooms = st.text_input("Number of Bathrooms", placeholder="e.g., 2")
sqft_living = st.text_input("Living Area (sqft)", placeholder="e.g., 2000")
sqft_lot = st.text_input("Lot Size (sqft)", placeholder="e.g., 5000")
floors = st.text_input("Number of Floors", placeholder="e.g., 1")
waterfront = st.selectbox("Waterfront (0 = No, 1 = Yes)", options=["Select", 0, 1])
view = st.selectbox("View Rating (0 = Poor, 4 = Excellent)", options=["Select", 0, 1, 2, 3, 4])
condition = st.selectbox("Condition (1 = Poor, 5 = Excellent)", options=["Select", 1, 2, 3, 4, 5])
sqft_above = st.text_input("Above Ground Area (sqft)", placeholder="e.g., 1500")
sqft_basement = st.text_input("Basement Area (sqft)", placeholder="e.g., 500")
yr_built = st.text_input("Year Built", placeholder="e.g., 2000")
yr_renovated = st.text_input("Year Renovated (0 if never)", placeholder="e.g., 0")
zip_encoded = st.text_input("Zip Code", placeholder="e.g., 98101")

# Predict button
if st.button("Predict House Price"):
    # Check for missing or invalid inputs
    try:
        # Convert inputs to proper data types
        data = {
            "bedrooms": float(bedrooms),
            "bathrooms": float(bathrooms),
            "sqft_living": float(sqft_living),
            "sqft_lot": float(sqft_lot),
            "floors": float(floors),
            "waterfront": int(waterfront),
            "view": int(view),
            "condition": int(condition),
            "sqft_above": float(sqft_above),
            "sqft_basement": float(sqft_basement),
            "yr_built": int(yr_built),
            "yr_renovated": int(yr_renovated),
            "zip_encoded": int(zip_encoded),
        }

        # API URL
        api_url = "http://127.0.0.1:5000/predict"

        # Call the API
        response = requests.post(api_url, json=data)

        # Check the response status
        if response.status_code == 200:
            result = response.json()
            predicted_price = result.get("predicted_price", "N/A")
            st.success(f"🏡 The predicted house price is **${predicted_price:,.2f}**")
            
            # Display the key factors affecting the prediction
            st.info("""
            **Key Factors for House Price Prediction:**
            - Square footage of the living area
            - Zip code of the property
            - Square footage of the lot
            - Year the property was built
            
            These factors mainly affect the price.
            """)

        else:
            st.error(f"Error: {response.json().get('error', 'Unknown error')}")
    except ValueError:
        st.error("Please provide valid numerical values for all inputs.")
    except Exception as e:
        st.error(f"An error occurred: {e}")


        # API URL
        api_url = "http://127.0.0.1:5000/predict"

        # Call the API
        response = requests.post(api_url, json=data)

        # Check the response status
        if response.status_code == 200:
            result = response.json()
            predicted_price = result.get("predicted_price", "N/A")
            st.success(f"🏡 The predicted house price is **${predicted_price:,.2f}**")
        else:
            st.error(f"Error: {response.json().get('error', 'Unknown error')}")
    except ValueError:
        st.error("Please provide valid numerical values for all inputs.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Footer
st.markdown("---")
st.markdown(
    "💡 *This app uses a machine learning model to predict house prices based on various input features.*"
)
