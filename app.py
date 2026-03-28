import streamlit as st
import joblib
import pandas as pd
import requests

# Load model and columns
model = joblib.load("\model\churn_model.pkl")
columns = joblib.load(r"\model\model_columns.pkl")

st.title("Customer Churn Prediction")

st.write("Enter customer details:")

# Simple inputs
tenure = st.slider("Tenure (months)", 0, 72)
monthly = st.number_input("Monthly Charges")

# Create input dataframe
input_df = pd.DataFrame([[tenure, monthly]], columns=["tenure", "MonthlyCharges"])

# Add missing columns
for col in columns:
    if col not in input_df:
        input_df[col] = 0

# Arrange columns
input_df = input_df[columns]


st.title("📊 Customer Churn Prediction")

tenure = st.slider("Tenure", 0, 72)
monthly = st.number_input("Monthly Charges")

if st.button("Predict"):
    
    url = "http://127.0.0.1:8000/predict"
    
    data = {
        "tenure": tenure,
        "MonthlyCharges": monthly
    }

    response = requests.post(url, json=data)

    result = response.json()

    if result["prediction"] == 1:
        st.error("⚠️ Customer will churn")
    else:
        st.success("✅ Customer will stay")
