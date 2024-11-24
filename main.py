import streamlit as st

# Title for the app
st.title("Welcome to Bangalore House Price Predictor")

# Description
st.write("Want to predict the price of a new House in Bangalore? Try filling the details below:")

# Input fields
location = st.selectbox("Select the Location:", ["6th Phase JP Nagar", "Whitefield", "Indiranagar", "Marathahalli"])
bhk = st.number_input("Enter BHK:", min_value=1, step=1)
bathrooms = st.number_input("Enter Number of Bathrooms:", min_value=1, step=1)
square_feet = st.number_input("Enter Total Square Feet:", min_value=500, step=100)

# Predict button
if st.button("Predict Price"):
    # Dummy prediction for testing
    predicted_price = 14352010.74  # Replace this with your prediction logic
    st.success(f"Prediction: ₹{predicted_price}")
