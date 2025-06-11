import streamlit as st
import joblib

# ✅ Page configuration (must be first Streamlit command)
st.set_page_config(
    page_title="RISERISE - Phishing URL Detector",
    page_icon="🔐",
    layout="centered"
)

# 🧠 Load ML model and vectorizer
model = joblib.load("models/phishing_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

# 🏷️ Title
st.title("🔐 RISERISE: Phishing URL Detector")
st.markdown("Check if a URL is potentially dangerous or safe.")

# 🔍 Input Section
st.subheader("🔗 Enter a URL to scan:")
url_input = st.text_input("Paste URL here...", placeholder="https://example.com")

# 🔎 Prediction
if st.button("Check URL"):
    if url_input:
        test_vector = vectorizer.transform([url_input])
        prediction = model.predict(test_vector)[0]

        # 🎯 Result Output
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
        st.warning("Please enter a valid URL.")
