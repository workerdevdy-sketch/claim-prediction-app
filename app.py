import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("claim_flag_model.pkl")

st.title("Insurance Claim Prediction")

year = st.number_input("Year")
month = st.number_input("Month")
cc = st.number_input("CC")
cylinder = st.number_input("Cylinder")
start_km = st.number_input("Start KM")
gross_premium = st.number_input("Gross Premium")
risk_premium = st.number_input("Risk Premium")

input_data = pd.DataFrame({
    "Year":[year],
    "Month":[month],
    "CC":[cc],
    "Cylinder":[cylinder],
    "Start KM":[start_km],
    "Gross Premium":[gross_premium],
    "Risk Premium":[risk_premium]
})

if st.button("Predict"):
    
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Claim Likely")
    else:
        st.success("No Claim Expected")
