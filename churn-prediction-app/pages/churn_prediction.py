import streamlit as st
import pandas as pd
import pickle

def load_model():
    with open("churn-prediction-app/models/model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

def churn_prediction_page():
    st.title("Customer Churn Prediction")
    
    st.write(
        """
        Enter the necessary details to predict whether a customer will churn or not.
    
        """
    )
    
    # User input form
    st.sidebar.subheader("Input Customer Data")
    feature_inputs = {}
    feature_names = ["Age", "Tenure", "Usage Frequency", "Support Calls", "Payment Delay", 
                     "Total Spend", "Last Interaction", "Subscription Type", "Contract Length", "Gender"]
    
    for feature in feature_names:
        feature_inputs[feature] = st.sidebar.number_input(f"Enter {feature}", value=0.0, step=0.1)
    
    # Convert input to dataframe
    input_df = pd.DataFrame([feature_inputs])
    
    if st.button("Predict Churn"):
        model = load_model()
        prediction = model.predict(input_df)[0]
        
        if prediction == 1:
            st.error("The customer is likely to churn.")
        else:
            st.success("The customer is not likely to churn.")
