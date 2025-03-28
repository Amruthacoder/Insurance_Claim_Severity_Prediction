import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("insurance_claim_best_model.pkl")

# Page Config
st.set_page_config(page_title="Insurance Claim Prediction", page_icon="🚗", layout="centered")

# Background Image (Fixed)
background_image_url = "https://img.freepik.com/free-photo/abstract-solid-shining-yellow-gradient-studio-wall-room-background_1258-71102.jpg?t=st=1743075597~exp=1743079197~hmac=10ab9d4a4cbacad87e576a88fad073152c2e832c953311a9f7eb4f38c790fc2d&w=2000"

st.markdown(
    f"""
    <style>
    .stApp {{
        background: url("{background_image_url}") no-repeat center center fixed;
        background-size: cover;
    }}
    .title {{
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        color: #0a74da;
    }}
    .stButton>button {{
        background-color: #0a74da !important;
        color: white !important;
        font-size: 16px !important;
    }}
    .custom-label {{
        font-size: 18px;
        font-weight: bold;
        color: black;  /* Ensuring black color for labels */
    }}
    .logo-container {{
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Load & Display Logo
logo_path = "/Users/amruthayenikonda/Desktop/Github Repo/Insurance-Claim-Severity-Prediction/Data/logo.jpg"
#st.image(logo_path, width=150)  # Adjust width as needed

col1, col2, col3 = st.columns([1, 2, 1])  # Adjust column widths as needed
with col2:
    st.image(logo_path, width=150)  # Centering the logo

# App Title
st.markdown('<p class="title">Insurance Claim Severity Prediction</p>', unsafe_allow_html=True)
st.markdown('<p class="custom-label">Enter details below to predict the claim amount:</p>', unsafe_allow_html=True)

# Input fields
st.markdown('<p class="custom-label">Annual Premium ($)</p>', unsafe_allow_html=True)
policy_annual_premium = st.number_input("", min_value=100, max_value=50000, value=2000)

st.markdown('<p class="custom-label">Vehicle Claim Amount ($)</p>', unsafe_allow_html=True)
vehicle_claim = st.number_input("", min_value=0, max_value=100000, value=5000)

st.markdown('<p class="custom-label">Months as Customer</p>', unsafe_allow_html=True)
months_as_customer = st.number_input("", min_value=1, max_value=300, value=20)

# Convert input to DataFrame
input_data = pd.DataFrame([{
    "policy_annual_premium": policy_annual_premium,
    "vehicle_claim": vehicle_claim,
    "months_as_customer": months_as_customer
}])

# Prediction Button
if st.button("Predict Claim Amount"):
    prediction = model.predict(input_data)
    st.markdown(
    f'<p style="font-size:20px; font-weight:bold; color:black;">💰 Predicted Insurance Claim Amount: ${prediction[0]:,.2f}</p>',
    unsafe_allow_html=True
)