from fastapi import FastAPI
import pickle
import pandas as pd

from Source.preprocess import preprocess_data

app = FastAPI()

model = pickle.load(open("Model/churn_model.pkl","rb"))
features = pickle.load(open("Model/model_features.pkl","rb"))


def risk_category(prob):

    if prob >= 0.7:
        return "High Risk"
    elif prob >= 0.4:
        return "Medium Risk"
    else:
        return "Low Risk"


@app.post("/predict")
def predict(data:dict):

    df = pd.DataFrame([data])

    df = preprocess_data(df)

    df = df.reindex(columns=features, fill_value=0)

    pred = model.predict(df)[0]
    prob = model.predict_proba(df)[0][1]

    risk = risk_category(prob)

    return {
        "prediction": int(pred),
        "churn_probability": float(prob),
        "risk_category": risk
    }