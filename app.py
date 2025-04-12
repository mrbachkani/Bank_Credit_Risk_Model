import streamlit as st
import numpy as np
import joblib

# Load the model
model = joblib.load("xgb_model.pkl")

# Define features manually — must match what model was trained on
feature_names = ['Duration', 'Credit_Amount', 'Age']

# UI
st.title("🏦 Credit Risk Prediction App")
st.markdown("Enter customer details to predict credit risk.")

# Collect input values
user_input = {}
user_input['Duration'] = st.slider("Loan Duration (months)", 6, 72, 12)
user_input['Credit_Amount'] = st.number_input("Credit Amount", 250, 20000, step=250)
user_input['Age'] = st.slider("Age", 18, 75, 30)

# Convert input to model format
input_array = np.array([[user_input[f] for f in feature_names]])

# Prediction
if st.button("Predict Credit Risk"):
    prediction = model.predict(input_array)[0]
    st.success(f"Prediction: {'❌ Bad Credit Risk' if prediction == 1 else '✅ Good Credit Risk'}")
