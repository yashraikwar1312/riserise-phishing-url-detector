import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Config & Logo
# -----------------------------
st.set_page_config(page_title="RISERISE - Phishing Detector", page_icon="🛡️", layout="centered")

st.markdown(
    """
    <style>
    body {
        background-color: #0f1117;
        color: #f1f1f1;
        font-family: 'Segoe UI', sans-serif;
    }
    .main {
        background-color: #1e2130;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 0 10px #00ffe5;
    }
    h1, h2 {
        color: #00ffe5;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.container():
    st.image("riserise_logo.png", width=150)  # Optional
    st.title("🛡️ RISERISE - Phishing URL Detector")
    st.markdown("Enter feature values of a URL to check if it's **Legitimate or Phishing**.")

# -----------------------------
# Load Model & Feature Names
# -----------------------------
@st.cache_resource
def load_model():
    model = joblib.load("phishing_model.joblib")
    features = joblib.load("model_features.joblib")
    return model, features

model, features = load_model()

# -----------------------------
# User Input Fields
# -----------------------------
user_input = {}
with st.form("phishing_form"):
    st.subheader("🔍 Enter URL Feature Values:")
    for feature in features:
        user_input[feature] = st.number_input(f"{feature}:", step=1.0)
    submitted = st.form_submit_button("🔐 Detect")

# -----------------------------
# Prediction Logic
# -----------------------------
if submitted:
    input_df = pd.DataFrame([user_input])
    prediction = model.predict(input_df)[0]
    result = "🔴 Phishing URL" if prediction == 1 else "🟢 Legitimate URL"

    st.subheader("✅ Prediction Result:")
    st.success(result if prediction == 0 else result, icon="🧠")

    st.markdown("---")
    st.caption("Model: Random Forest | Built with ❤️ by Yash")
