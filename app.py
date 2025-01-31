import streamlit as st
from pages.about import about_page
from pages.churn_prediction import churn_prediction_page

# Custom CSS Styling for Enhanced UI
st.markdown(
    """
    <style>
    .main-title {
        font-size: 40px;
        font-weight: bold;
        color: #2E3B4E;
        text-align: center;
        margin-bottom: 20px;
    }
    .nav-bar {
        background-color: #007BFF;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
    }
    .nav-link {
        font-size: 18px;
        font-weight: bold;
        color: white;
        text-decoration: none;
        padding: 8px 16px;
        border-radius: 5px;
        display: inline-block;
        margin: 5px;
    }
    .nav-link:hover {
        background-color: #0056b3;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main Title
st.markdown('<p class="main-title">📊 Customer Churn Prediction App</p>', unsafe_allow_html=True)

# Navigation Bar
st.markdown('<div class="nav-bar">', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🏠 Home"):
        st.experimental_set_query_params(page="about")

with col2:
    if st.button("📈 Dashboard"):
        st.experimental_set_query_params(page="dashboard")

with col3:
    if st.button("🔮 Prediction"):
        st.experimental_set_query_params(page="prediction")

st.markdown("</div>", unsafe_allow_html=True)

# Handle Page Navigation
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["about"])[0]

if page == "about":
    about_page()
elif page == "prediction":
    churn_prediction_page()
else:
    about_page()
