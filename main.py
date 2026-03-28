from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Load model
model = joblib.load(r"C:\Users\manns\OneDrive\Desktop\Project\model\churn_model.pkl")
columns = joblib.load(r"C:\Users\manns\OneDrive\Desktop\Project\model\model_columns.pkl")


# Health check
@app.get("/")
def home():
    return {"message": "Churn API is running 🚀"}


# Prediction endpoint
@app.post("/predict")
def predict(data: dict):
    
    # Convert input to dataframe
    input_df = pd.DataFrame([data])

    # Add missing columns
    for col in columns:
        if col not in input_df:
            input_df[col] = 0

    input_df = input_df[columns]

    # Prediction
    prediction = model.predict(input_df)

    return {
        "prediction": int(prediction[0])
    }