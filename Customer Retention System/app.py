import streamlit as st
import requests

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction System")
st.markdown("Predict whether a telecom customer is likely to churn.")

# Sidebar for inputs
st.sidebar.header("Customer Information")

gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
senior = st.sidebar.selectbox("Senior Citizen", [0, 1])
partner = st.sidebar.selectbox("Partner", ["Yes", "No"])
dependents = st.sidebar.selectbox("Dependents", ["Yes", "No"])
tenure = st.sidebar.slider("Tenure (months)", 1, 72)
phone = st.sidebar.selectbox("Phone Service", ["Yes", "No"])
monthly = st.sidebar.number_input("Monthly Charges", min_value=0.0)
total = st.sidebar.number_input("Total Charges", min_value=0.0)

st.subheader("Customer Input Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Gender", gender)
col2.metric("Tenure (Months)", tenure)
col3.metric("Monthly Charges", monthly)

st.markdown("---")

if st.button("🔍 Predict Churn"):

    data = {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone,
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=data
    )

    result = response.json()

    st.subheader("Prediction Result")

    prob = result["churn_probability"]
    risk = result["risk_category"]

    col1, col2 = st.columns(2)

    col1.metric("Churn Probability", f"{prob:.2f}")

    if risk == "High Risk":
        col2.error(f"⚠ {risk}")
    elif risk == "Medium Risk":
        col2.warning(f"⚡ {risk}")
    else:
        col2.success(f"✅ {risk}")