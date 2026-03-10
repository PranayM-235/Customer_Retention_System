# Customer Retention Intelligence System
### Project Overview

The Customer Retention Intelligence System is an end-to-end machine learning project designed to predict whether a telecom customer is likely to churn.

The system analyzes customer attributes such as tenure, service usage, and billing details to estimate the probability of churn and classify customers into risk categories.

## The project demonstrates a complete data science workflow including:

### 1. Data preprocessing

Machine learning model training

Handling class imbalance

Model API development

Interactive prediction dashboard

## Tech Stack

Programming Language

Python

Libraries

pandas

scikit-learn

matplotlib

imbalanced-learn

Frameworks

FastAPI

Streamlit

Machine Learning Model

Random Forest

Dataset

The project uses the telecom customer dataset containing customer demographics, service usage, and billing information.

Target Variable:

Churn

1 → Customer leaves the company

0 → Customer stays with the company

Project Structure
Customer Retention System
│
├── Data
│   └── Telco_CustChurn.csv
│
├── Model
│   ├── churn_model.pkl
│   └── model_features.pkl
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
Folder Explanation
Data

Contains the dataset used for training the machine learning model.

Telco_CustChurn.csv

Telecom customer dataset used for churn prediction.

Model

Stores the trained machine learning model files.

churn_model.pkl

Trained Random Forest model used for predictions.

model_features.pkl

List of feature columns used during model training to maintain consistency during prediction.

Source

Contains the core machine learning logic.

preprocess.py

Handles data cleaning and preprocessing

Converts categorical values into numerical format

Ensures the dataset is ready for model training

train.py

Loads dataset

Applies preprocessing

Handles class imbalance using SMOTE

Trains the Random Forest model

Saves the trained model and feature list

predict.py

Loads the trained model

Accepts new customer data

Performs preprocessing

Returns churn probability and risk category

api.py

Implements the backend API using FastAPI.

Responsibilities:

Accepts input data from the dashboard

Sends the data to the prediction pipeline

Returns churn prediction results

app.py

Creates an interactive dashboard using Streamlit.

Features:

User input form for customer details

Sends request to FastAPI backend

Displays prediction results including:

churn probability

risk category

Machine Learning Workflow

Load dataset

Data preprocessing

Train-test split

Handle class imbalance using SMOTE

Train Random Forest model

Save trained model

Create API for predictions

Build dashboard for user interaction

Example Prediction Output
Churn Probability: 0.78
Risk Category: High Risk
How to Run the Project
Install dependencies
pip install -r requirements.txt
Train the model
python Source/train.py
Run FastAPI server
uvicorn api:app --reload
Run Streamlit dashboard
streamlit run app.py
Business Impact

This system helps companies:

Identify customers likely to churn

Take preventive retention actions

Improve customer lifetime value

Reduce revenue loss

Author

Pranay S Masurkar

✅ This version is better because

it matches your actual project folders

recruiters can understand the architecture quickly

it looks like a real production project