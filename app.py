# ✅ Set page config FIRST before any other Streamlit function
import streamlit as st
st.set_page_config(
    page_title="RISERISE - Phishing URL Detector",
    page_icon="🔐",
    layout="centered"
)

# ✅ Now it's safe to import everything else
from streamlit_lottie import st_lottie
import json
import joblib
import re

# 🔄 Load Lottie animation
def load_lottie(path: str):
    with open(path, "r") as f:
        return json.load(f)

# Load animation and models
lottie_animation = load_lottie("assets/animations.json")
model = joblib.load("models/phishing_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

# 🧠 Interface
st_lottie(lottie_animation, speed=1, height=250, key="riserise-anim")
st.title("🔐 RISERISE: Phishing URL Detector")
st.markdown("Protect yourself from phishing attacks with our ML-powered URL checker!")

# 🔍 URL Input
st.subheader("🔗 Check a Suspicious URL")
url_input = st.text_input("Paste a URL here:", placeholder="https://example.com")

# 🔎 Prediction
if st.button("Check URL"):
    if url_input:
        test_vector = vectorizer.transform([url_input])
        prediction = model.predict(test_vector)[0]

        # 🎯 Output result with color
        if prediction == 1:
            st.markdown(
                f"<p style='color:red;font-weight:bold;'>⚠️ This URL is likely <u>Phishing</u>: <a href='{url_input}' style='color:red;' target='_blank'>{url_input}</a></p>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"<p style='color:green;font-weight:bold;'>✅ This URL appears <u>Safe</u>: <a href='{url_input}' style='color:green;' target='_blank'>{url_input}</a></p>",
                unsafe_allow_html=True
            )
    else:
        st.warning("Please paste a URL to check.")
