import streamlit as st
import pandas as pd

def about_page():
    # Custom Styling
    st.markdown(
        """
        <style>
        .big-title {
            font-size: 32px;
            font-weight: bold;
            color: #4A90E2;
            text-align: center;
        }
        .sub-title {
            font-size: 20px;
            font-weight: bold;
            color: #555;
        }
        .card {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<p class="big-title">About Customer Churn Prediction App</p>', unsafe_allow_html=True)

    # App Description
    st.write(
        """
        This application predicts **customer churn** using **Machine Learning**.
        We trained an **XGBoost model** on historical customer data to detect the probability of churn.
        """
    )

    # Machine Learning Details
    st.markdown('<p class="sub-title">🔍 Machine Learning Approach</p>', unsafe_allow_html=True)
    st.markdown(
        """
        - **Model Used:** XGBoost Classifier  
        - **Features:** 10 key factors based on domain knowledge  
        - **Performance:** High accuracy & recall for reliable churn detection  
        """
    )

    # Sample Dataset
    try:
        df = pd.read_csv('data/customer_churn_dataset.csv')
        st.markdown('<p class="sub-title">📊 Sample Training Data</p>', unsafe_allow_html=True)
        st.dataframe(df.head(), use_container_width=True, height=200)
    except FileNotFoundError:
        st.error("❌ Sample dataset not found! Please ensure 'data/sample_data.csv' exists.")

