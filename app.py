import streamlit as st import pandas as pd import joblib

Load model and features

model = joblib.load("phishing_model.joblib") features = joblib.load("model_features.joblib")

Set page config

st.set_page_config(page_title="RISERISE - Phishing URL Detector", page_icon="🛡️", layout="centered")

Cybersecurity theme styling

st.markdown( """ <style> body { background-color: #0f111a; color: #c7c7c7; } .stButton>button { background-color: #1f2937; color: white; border-radius: 8px; padding: 0.5em 1em; } .stTextInput>div>div>input { background-color: #1f1f2e; color: white; } </style> """, unsafe_allow_html=True )

Title

st.title("🛡️ RISERISE") st.subheader("Phishing URL Detection Tool")

Instruction

st.markdown("Enter the website feature details to check if it's phishing or safe.")

Input form

with st.form("url_form"): input_data = {} for col in features: dtype = float if "Ratio" in col or "Score" in col or "Length" in col or col.startswith("NoOf") else int val = st.text_input(f"{col}:") try: input_data[col] = dtype(val) except: input_data[col] = 0  # fallback default submitted = st.form_submit_button("Check")

Prediction

if submitted: try: df = pd.DataFrame([input_data]) prediction = model.predict(df)[0] if prediction == 1: st.error("🚨 This URL is phishing.") else: st.success("✅ This URL is legitimate.") except Exception as e: st.warning(f"Prediction failed: {e}")

