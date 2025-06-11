import streamlit as st
import joblib
import re
from streamlit_lottie import st_lottie
import json

# Load animation
def load_lottie(path: str):
    with open(path, 'r') as f:
        return json.load(f)

# Load Model
model = joblib.load('phishing_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Page Config
st.set_page_config(page_title="RISERISE - Phishing URL Detector", page_icon="🔐", layout="centered")

# Background Animation
lottie_animation = load_lottie("assets/animations.json")

# Title Section
st_lottie(lottie_animation, speed=1, height=250)
st.title("🔐 RISERISE: Phishing URL Detector")
st.markdown("Protect yourself from phishing attacks with our ML-powered URL checker!")

# Input
url_input = st.text_input("🔗 Enter a URL to check:")

if st.button("Check"):
    if url_input:
        test_vector = vectorizer.transform([url_input])
        prediction = model.predict(test_vector)[0]
        if prediction == 1:
            st.error("⚠️ This is likely a **phishing** website!")
        else:
            st.success("✅ This appears to be a **safe** website.")
    else:
        st.warning("Please enter a URL.")
