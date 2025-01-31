# Customer Churn Prediction App

This is a customer churn prediction application developed using **Streamlit**. The app predicts whether a customer is likely to churn (leave) based on various factors such as account information, usage data, and customer interactions.

## Overview

In this project, two machine learning algorithms;**Random Forest** and **XGBoost** were used to train the models. The app utilizes the **XGBoost** algorithm for making predictions. The model was trained on historical data, and it provides businesses with a tool to identify customers who may need special attention to prevent churn.

## Features

- User-friendly interface using **Streamlit** for easy customer churn prediction.
- Input fields for customer data such as age, account type, usage statistics, etc.
- Predictive output showing the likelihood of customer churn.
- Model performance evaluation using various metrics.

## Installation

To run the app locally, you need to set up the environment and install the required libraries. Here's how:

### 1. Clone the repository:
```bash
git clone https://github.com/nethmiidesilva/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Run the app:
```bash
streamlit run app.py
```

The app will open in your web browser, allowing you to interact with it and make predictions.

## Algorithms Used

- **Random Forest**: This algorithm was trained as a comparison to evaluate model performance.
- **XGBoost**: The final model used in the application, known for its superior performance in classification tasks.

## Model Performance

Both models were evaluated using accuracy, precision, recall, and F1-score to ensure their effectiveness in predicting customer churn. The XGBoost model showed better performance and was selected for use in the Streamlit app.
