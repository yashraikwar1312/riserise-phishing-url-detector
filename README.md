# 🔐 RISERISE - Phishing URL Detection Tool

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/streamlit-live-green)

RISERISE is a machine learning-powered phishing URL detection tool designed to identify suspicious or malicious websites and protect users from phishing attacks. With a simple and elegant web interface powered by Streamlit, it allows real-time evaluation of URLs and alerts users if a site is potentially harmful.

## 📌 Problem Statement

Phishing websites trick users into revealing sensitive information such as passwords, credit card numbers, and other personal data. Identifying these websites manually is often impossible due to their deceptive appearance.

## 🎯 Objectives

- Develop a tool that classifies URLs as **phishing** or **legitimate**.
- Use **Machine Learning** for accurate detection.
- Provide an easy-to-use **web interface** for checking URLs.
- Deploy it with an **interactive UI and animations** using Streamlit.

## 🛠️ Features

- 🔍 Real-time phishing detection from URL input
- ✅ Trained with a labeled dataset of phishing and legitimate URLs
- 📊 Built with Scikit-learn (Logistic Regression)
- 🎨 Animated and responsive UI using **Lottie animations**
- 🌐 Deployed on **Streamlit Cloud**

## 🚀 Live Demo

👉 [Click here to try RISERISE on Streamlit](#)

## 📂 Folder Structure

```
riserise-phishing-url-detector/
├── app.py
├── phishing_model.pkl
├── vectorizer.pkl
├── requirements.txt
├── assets/
│   └── animations.json
└── README.md
```

## 📊 Model & Dataset

- **Dataset**: A labeled dataset of phishing and legitimate URLs (CSV format)
- **Vectorization**: CountVectorizer (Bag of Words)
- **Algorithm**: Logistic Regression (simple and effective)
- **Accuracy**: Achieved ~90% on test data

## 📦 Installation & Local Run

```bash
git clone https://github.com/<your-username>/riserise-phishing-url-detector.git
cd riserise-phishing-url-detector
pip install -r requirements.txt
streamlit run app.py
```

## 🖼️ Screenshots

> Add screenshots of the app interface once deployed for better visualization

## 💡 Future Improvements

- Use advanced models like XGBoost or Neural Networks
- Implement browser extension version
- Add URL shortening and redirection tracing
- Introduce live scanning from email/snippet input

## 🤝 Contributing

Pull requests are welcome! If you have suggestions for improvements or new features, feel free to fork the repo and open a PR.

## 🛡️ License

This project is licensed under the [MIT License](LICENSE).

## 👤 Author

**Yash Raikwar**  
📧 yashraikwar132005@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/yash-raikwar-7504632a2) | [GitHub](https://github.com/yashraikwar1312) | [Twitter](https://x.com/yashraikwar2005)

## 🙏 Acknowledgements

- Streamlit Team for the awesome framework
- LottieFiles for free and creative animations
- Scikit-learn and the open-source ML community
