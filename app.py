import streamlit as st
import joblib

# Load model
model = joblib.load("model.pkl")

# Page config
st.set_page_config(page_title="House Price Predictor", layout="centered")

# Title
st.title("🏠 House Price Prediction App")
st.write("Enter details below to predict house price")

# Inputs in columns
col1, col2 = st.columns(2)

with col1:
    size = st.number_input("📏 Size (sq ft)", min_value=0)

with col2:
    rooms = st.number_input("🛏 Rooms", min_value=0)

age = st.number_input("🏗 Age of house", min_value=0)

# Button
if st.button("🔍 Predict Price"):

    if rooms == 0:
        st.error("Rooms cannot be 0 ❌")
    else:
        size_per_room = size / rooms
        result = model.predict([[size, rooms, age, size_per_room]])

        st.success(f"💰 Predicted Price: {result[0]:.2f} Lakhs")