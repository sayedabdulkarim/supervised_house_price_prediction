import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the Ridge model pipeline
with open("RidgeModel.pkl", "rb") as model_file:
    pipe = pickle.load(model_file)

# Load the cleaned data to get location options
data = pd.read_csv("Cleaned_data.csv")
locations = sorted(data['location'].unique())

# Title for the app
st.title("Welcome to Bangalore House Price Predictor")

# Description
st.write("Want to predict the price of a new House in Bangalore? Try filling the details below:")

# Input fields
location = st.selectbox("Select the Location:", locations)
bhk = st.number_input("Enter BHK:", min_value=1, step=1)
bathrooms = st.number_input("Enter Number of Bathrooms:", min_value=1, step=1)
square_feet = st.number_input("Enter Total Square Feet:", min_value=500, step=100)

# Predict button
if st.button("Predict Price"):
    try:
        # Prepare input for the pipeline
        input_data = pd.DataFrame({
            "location": [location],
            "total_sqft": [square_feet],
            "bath": [bathrooms],
            "bhk": [bhk]
        })

        # Make a prediction using the pipeline
        prediction = pipe.predict(input_data)[0]

        # Display the prediction
        st.success(f"Predicted Price: ₹{round(prediction, 2)}")
    except Exception as e:
        st.error(f"Error making prediction: {e}")
