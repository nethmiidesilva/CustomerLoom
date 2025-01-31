import streamlit as st
import numpy as np
import pickle

# Load Model
with open("models/model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

def predict_churn(features):
    """Function to predict churn using the trained model"""
    features_array = np.array(features).reshape(1, -1)
    prediction = model.predict(features_array)
    return "❌ Churn" if prediction[0] == 1 else "✅ Not Churn"

def churn_prediction_page():
    st.markdown(
        """
        <style>
        .big-title {
            font-size: 32px;
            font-weight: bold;
            color: #E91E63;
            text-align: center;
        }
        .form-container {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            margin: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<p class="big-title">🔮 Customer Churn Prediction</p>', unsafe_allow_html=True)
    
    with st.form("churn_form"):
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        st.write("### ✍️ Enter Customer Details:")

        # Example: Collecting 10 features
        Age = st.number_input("📌 Age", value=0.0)
        Tenure = st.number_input("📌 Tenure", value=0.0)
        feature_3 = st.number_input("📌 Feature 3", value=0.0)
        feature_4 = st.number_input("📌 Feature 4", value=0.0)
        feature_5 = st.number_input("📌 Feature 5", value=0.0)
        feature_6 = st.number_input("📌 Feature 6", value=0.0)
        feature_7 = st.number_input("📌 Feature 7", value=0.0)
        feature_8 = st.number_input("📌 Feature 8", value=0.0)
        feature_9 = st.number_input("📌 Feature 9", value=0.0)
        feature_10 = st.number_input("📌 Feature 10", value=0.0)

        # Submit button
        submitted = st.form_submit_button(" Predict")

    if submitted:
        features = [feature_1, feature_2, feature_3, feature_4, feature_5, 
                    feature_6, feature_7, feature_8, feature_9, feature_10]

        result = predict_churn(features)
        st.success(f"🎯 Prediction: **{result}**")
