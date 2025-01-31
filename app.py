import streamlit as st
from pages.about import about_page
from pages.churn_prediction import churn_prediction_page

# Apply Streamlit Theme & Custom Styling
st.set_page_config(page_title="Churn Prediction App", layout="wide")

st.markdown(
    """
    <style>
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #1E1E1E;
    }
    .sidebar-title {
        font-size: 26px;
        font-weight: bold;
        color: #FFFFFF;
        text-align: center;
    }
    .sidebar-nav {
        font-size: 18px;
        font-weight: bold;
        color: white;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        cursor: pointer;
    }
    .sidebar-nav:hover {
        background-color: #007BFF;
        color: white;
    }
    /* Main Page Styling */
    .main-title {
        font-size: 40px;
        font-weight: bold;
        color: #2E3B4E;
        text-align: center;
        margin-bottom: 20px;
    }
    .content-container {
        background-color: #F8F9FA;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    /* Machine Learning Approach Styling */
    .ml-title {
        font-size: 28px;
        font-weight: bold;
        color: #FF5733; /* Orange */
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        text-align: center;
        margin-bottom: 10px;
    }
    .ml-content {
        font-size: 20px;
        color: #333;
        text-align: justify;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar Navigation
st.sidebar.markdown('<p class="sidebar-title">🔍 Navigation</p>', unsafe_allow_html=True)
page_selection = st.sidebar.radio("", ["🏠 About", "🔮 Prediction"], index=0)

# Main Title
st.markdown('<p class="main-title">📊 Customer Churn Prediction App</p>', unsafe_allow_html=True)
st.markdown('<div class="content-container">', unsafe_allow_html=True)

# Display Selected Page
if page_selection == "🏠 About":
    about_page()
elif page_selection == "🔮 Prediction":
    churn_prediction_page()

st.markdown("</div>", unsafe_allow_html=True)
