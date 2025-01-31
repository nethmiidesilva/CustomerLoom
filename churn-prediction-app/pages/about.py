import streamlit as st
import pandas as pd

def about_page():
    st.title("About Customer Churn Prediction App")
    
    st.write(
        """
        This application is designed to predict customer churn using machine learning.
        We have trained an XGBoost model on historical customer data to determine the likelihood
        of churn based on various factors like usage behavior, subscription details, and demographics.
        """
    )
    
    st.write("### Machine Learning Approach")
    st.write(
        """
        - Model Used: XGBoost Classifier
        - Features: 10 key features selected based on domain knowledge and feature importance analysis.
        - Performance: Achieved high accuracy and recall, ensuring effective churn prediction.
        """
    )
    
    # Display a sample dataset
    try:
        df = pd.read_csv('churn-prediction-app/data/customer_churn_dataset.csv')
        st.write("### Sample Training Data")
        st.write(df.head())
    except FileNotFoundError:
        st.write("Sample dataset not found. Please ensure 'data/sample_data.csv' exists.")
