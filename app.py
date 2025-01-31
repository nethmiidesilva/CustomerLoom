import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("models/model.pkl", "rb") as file:
    model = pickle.load(file)

# Set page config
st.set_page_config(page_title="Customer Churn Prediction", page_icon=":guardsman:", layout="centered")

# Apply custom styles
st.markdown(
    """
    <style>
        .title {
            color: brown;
            font-size: 50px !important;
            font-weight: bold;
            text-align: center;
        }
        .intro {
            color: #A67B5B;
            font-size: 24px;
            text-align: center;
            line-height: 1.6;
        }
        .predict-btn {
            background-color: red !important;
            color: white !important;
            font-size: 20px !important;
            padding: 10px 20px !important;
            border-radius: 10px !important;
            font-weight: bold !important;
            display: block;
            margin: auto;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# App Title
st.markdown('<p class="title">Customer Churn Prediction</p>', unsafe_allow_html=True)

# Intro Section
st.markdown(
    '<p class="intro">This application helps businesses predict customer churn based on various factors such as usage behavior, payment history, and customer engagement. By analyzing key metrics, businesses can take proactive steps to retain valuable customers and improve service quality. Simply enter the required details below and get an instant prediction of whether a customer is likely to churn or stay.</p>',
    unsafe_allow_html=True,
)

st.markdown("---")

# User Inputs
age = st.slider("Age", 18, 60, 30)
gender = st.selectbox("Gender", ["Male", "Female"])
tenure = st.slider("Tenure (Months)", 1, 60, 12)
usage_frequency = st.slider("Usage Frequency (Times/Month)", 1, 30, 15)
support_calls = st.slider("Support Calls", 0, 10, 2)
payment_delay = st.slider("Payment Delay (Days)", 0, 30, 5)
subscription_type = st.selectbox("Subscription Type", ["Basic", "Standard", "Premium"])
contract_length = st.selectbox("Contract Length", ["Monthly", "Quarterly", "Annual"])
total_spend = st.slider("Total Spend ($)", 100, 1000, 500)
last_interaction = st.slider("Last Interaction (Days Ago)", 1, 30, 10)

# Prepare input data
input_data = np.array([0, age, tenure, usage_frequency, support_calls, payment_delay, total_spend, last_interaction
]).reshape(1, -1)

# Predict button
if st.button("Predict Churn", key="predict", help="Click to get the prediction", use_container_width=True):
    prediction = model.predict(input_data)
    result = "Customer is likely to churn" if prediction[0] == 1 else "Customer is likely to stay"
    st.markdown(f'<p style="text-align: center; font-size: 24px; color: black; font-weight: bold;">{result}</p>', unsafe_allow_html=True)
