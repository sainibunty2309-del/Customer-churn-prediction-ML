import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load("churn_model.pkl")
label_encoders = joblib.load("label_encoders.pkl")

st.title("Customer Churn Prediction")

gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", ["Yes", "No"])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.number_input("Tenure Months", 0, 100, 12)
phone = st.selectbox("Phone Service", ["Yes", "No"])
multiple = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
online_backup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])
device = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
tech = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
movies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
payment = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)
monthly = st.number_input("Monthly Charges", 0.0, 1000.0, 70.0)
total = st.number_input("Total Charges", 0.0, 100000.0, 1000.0)

if st.button("Predict"):

    input_df = pd.DataFrame({
        "Gender": [gender],
        "Senior Citizen": [senior],
        "Partner": [partner],
        "Dependents": [dependents],
        "Tenure Months": [tenure],
        "Phone Service": [phone],
        "Multiple Lines": [multiple],
        "Internet Service": [internet],
        "Online Security": [online_security],
        "Online Backup": [online_backup],
        "Device Protection": [device],
        "Tech Support": [tech],
        "Streaming TV": [tv],
        "Streaming Movies": [movies],
        "Contract": [contract],
        "Paperless Billing": [paperless],
        "Payment Method": [payment],
        "Monthly Charges": [monthly],
        "Total Charges": [total]
    })

    # Encode categorical columns
    for col in input_df.columns:
        if col in label_encoders:
            input_df[col] = label_encoders[col].transform(input_df[col])

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("⚠️ Customer is likely to churn.")
    else:
        st.success("✅ Customer is likely to stay.")