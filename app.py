import streamlit as st
import pickle

# ------------------ SETTINGS ------------------ #
st.set_page_config(page_title="RISERISE st.image("riserise_logo.png", width=200) - Phishing Detector", page_icon="🛡️", layout="centered")

# ------------------ CSS STYLING ------------------ #
st.markdown("""
    <style>
    body {
        background-color: #0d1117;
        color: #e6edf3;
    }
    .main {
        background-color: #0d1117;
    }
    h1, h2, h3, h4 {
        color: #58a6ff;
    }
    .stTextInput>div>div>input {
        background-color: #161b22;
        color: white;
        border: 1px solid #30363d;
    }
    .stButton>button {
        background-color: #238636;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1.2em;
        font-weight: bold;
    }
    .stRadio > div {
        background-color: #161b22;
        color: white;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------ #
st.title("🛡️ RISERISE")
st.markdown("### Smart Phishing URL Detection")
st.markdown("_Protecting users from malicious websites using Machine Learning._")

# ------------------ MODEL LOADING ------------------ #
@st.cache_resource
def load_model_and_vectorizer():
    with open("phishing_model.pkl", "rb") as model_file, open("vectorizer.pkl", "rb") as vec_file:
        model = pickle.load(model_file)
        vectorizer = pickle.load(vec_file)
    return model, vectorizer

def predict_url_ml(url, model, vectorizer):
    features = vectorizer.transform([url])
    prediction = model.predict(features)[0]
    return "Phishing" if prediction == 1 else "Legitimate"

model, vectorizer = load_model_and_vectorizer()

# ------------------ INPUT SECTION ------------------ #
st.markdown("#### 🔍 Enter the URL you want to scan:")
url = st.text_input("Example: http://free-prizes.win/verify")

if st.button("🚀 Scan Now"):
    if url.strip() == "":
        st.warning("Please enter a URL.")
    else:
        with st.spinner("Analyzing URL... 🔐"):
            result = predict_url_ml(url, model, vectorizer)

        if result == "Phishing":
            st.error("⚠️ This URL is likely **Phishing**. Avoid clicking!")
        else:
            st.success("✅ This URL is **Legitimate**.")

# ------------------ FOOTER ------------------ #
st.markdown("---")
st.caption("🔒 Built for Cybersecurity Awareness | © 2025 RISERISE")
