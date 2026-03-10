import pickle
import pandas as pd
from preprocess import preprocess_data

# Load model
model = pickle.load(open("Model/churn_model.pkl", "rb"))

# Load feature columns
model_features = pickle.load(open("Model/model_features.pkl", "rb"))


def risk_category(prob):

    if prob >= 0.7:
        return "High Risk"
    elif prob >= 0.4:
        return "Medium Risk"
    else:
        return "Low Risk"


def predict_customer(data):

    df = pd.DataFrame([data])

    df = preprocess_data(df)

    # Align columns with training features
    df = df.reindex(columns=model_features, fill_value=0)

    pred = model.predict(df)[0]
    prob = model.predict_proba(df)[0][1]

    risk = risk_category(prob)

    return {
        "prediction": int(pred),
        "churn_probability": float(prob),
        "risk_category": risk
    }


# Test input
sample_customer = {
    "gender": "Male",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 12,
    "PhoneService": "Yes",
    "MonthlyCharges": 70,
    "TotalCharges": 800
}

result = predict_customer(sample_customer)

print(result)