import streamlit as st
from pages.about import about_page
from pages.churn_prediction import churn_prediction_page

def main():
    # Sidebar navigation
    st.sidebar.image("churn-prediciton-app/assets/logo.jpg", width=200)
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["About", "Churn Prediction"])
    
    # Display selected page
    if page == "About":
        about_page()
    elif page == "Churn Prediction":
        churn_prediction_page()

if __name__ == "__main__":
    main()
