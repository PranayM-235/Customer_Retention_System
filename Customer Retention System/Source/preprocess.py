import pandas as pd

def preprocess_data(df):

    df = df.copy()

    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
        df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

    if "customerID" in df.columns:
        df = df.drop("customerID", axis=1)

    if "Churn" in df.columns:
        df["Churn"] = df["Churn"].map({"No":0,"Yes":1})

    cat_cols = df.select_dtypes(include="object").columns
    df = pd.get_dummies(df, columns=cat_cols, drop_first=True)

    df = df.fillna(0)

    return df