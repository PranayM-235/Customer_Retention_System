# Customer Retention Intelligence System

## Project Overview

The **Customer Retention Intelligence System** is an end-to-end machine learning project designed to predict whether a telecom customer is likely to churn.

The system analyzes customer attributes such as tenure, service usage, and billing information to estimate churn probability and classify customers into risk categories.

This project demonstrates a complete **data science workflow** including data preprocessing, machine learning model training, API development, and dashboard visualization.

---

## Tech Stack

**Programming Language**

- Python

**Libraries**

- pandas
- scikit-learn
- matplotlib
- imbalanced-learn

**Frameworks**

- FastAPI
- Streamlit

**Machine Learning Model**

- Random Forest Classifier

---

## Dataset

The project uses a telecom customer dataset containing customer demographics, services subscribed, billing information, and churn status.

**Target Variable**

- `Churn = 1` → Customer leaves the company  
- `Churn = 0` → Customer stays with the company  

---

## Project Structure

```
Customer Retention System
│
├── Data
│   └── Telco_CustChurn.csv
│
├── Model
│
├── Source
│   ├── preprocess.py
│   ├── train.py
│   └── predict.py
│
├── api.py
├── app.py
├── requirements.txt
└── README.md
```

---

## System Architecture

User enters customer information through the dashboard.

Streamlit sends the request to the FastAPI backend.

FastAPI processes the request and sends data to the trained machine learning model.

The model predicts churn probability and returns the result to the dashboard.

---

## Machine Learning Workflow

1. Load dataset
2. Perform data preprocessing
3. Split dataset into training and testing sets
4. Handle class imbalance using SMOTE
5. Train Random Forest model
6. Save trained model
7. Build API for prediction
8. Create dashboard for user interaction

---

## Example Prediction Output

```
Churn Probability: 0.78
Risk Category: High Risk
```

---

## How to Run the Project

### 1 Install Dependencies

```
pip install -r requirements.txt
```

### 2 Train the Model

```
python Source/train.py
```

### 3 Run FastAPI Server

```
uvicorn api:app --reload
```

### 4 Run Streamlit Dashboard

```
streamlit run app.py
```

---

## Business Impact

This system helps companies:

- Identify customers likely to churn
- Take preventive retention actions
- Improve customer lifetime value
- Reduce revenue loss

---

## Future Improvements

- Deploy the system on cloud
- Add real-time prediction API
- Improve model performance using advanced algorithms
- Add explainable AI (SHAP)

