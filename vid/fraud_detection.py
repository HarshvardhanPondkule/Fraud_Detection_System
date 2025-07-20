import streamlit as st
import pandas as pd
import joblib
import os 

# Load the model
current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, "fraud_detection_pipeline.pkl")
model = joblib.load(model_path)


# Title and description
st.title("Fraud_Detection_System")
st.markdown("Please enter the transaction details and use the predict button")

st.divider()

# Input fields
transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])

amount = st.number_input("Amount", min_value=0.0, value=1000.0)

oldbalanceorg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)

newbalanceorg = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)

oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)

newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

# Predict button
if st.button("Predict"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceorg,
        "newbalanceOrig": newbalanceorg,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    prediction = model.predict(input_data)[0]
    st.subheader(f"Prediction: '{int(prediction)}'")

    if prediction == 1:
        st.error("This transaction can be fraud")
    else:
        st.success("This transaction looks like it is not a fraud")
