
import streamlit as st
import joblib
import numpy as np

# Load the trained Random Forest model
model = joblib.load("random_forest_model.pkl")

st.title("🌦️ Weather Prediction App")
st.write("Enter today's weather data to predict whether it will rain tomorrow.")

# Replace these fields with your actual model input features
MinTemp = st.number_input("Min Temperature (°C)")
MaxTemp = st.number_input("Max Temperature (°C)")
Rainfall = st.number_input("Rainfall (mm)")
Humidity3pm = st.number_input("Humidity at 3pm (%)")
Pressure3pm = st.number_input("Pressure at 3pm (hPa)")
WindSpeed3pm = st.number_input("Wind Speed at 3pm (km/h)")
Temp3pm = st.number_input("Temperature at 3pm (°C)")

# Predict button
if st.button("Predict"):
    input_data = np.array([[MinTemp, MaxTemp, Rainfall, Humidity3pm, Pressure3pm, WindSpeed3pm, Temp3pm]])
    prediction = model.predict(input_data)
    result = "🌧️ Yes, it will rain tomorrow." if prediction[0] == 1 else "☀️ No, it won't rain tomorrow."
    st.success(result)
