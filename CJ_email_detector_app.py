import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("email_detection_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

def main():
    st.title("Email Phishing Detection System")
    
    # Input area
    email_text = st.text_area("Enter the email body below:")

    # Predict button
    if st.button("Check Email"):
        if email_text.strip() == "":
            st.warning("Please enter an email to analyze.")
        else:
            # Transform the input
            X_input = vectorizer.transform([email_text])
            prediction = model.predict(X_input)[0]
            probability = model.predict_proba(X_input)[0]

            if prediction == 1:
                st.error(f"🚨 Phishing Email Detected! (Confidence: {probability[1]*100:.2f}%)")
            else:
                st.success(f"✅ Legitimate Email (Confidence: {probability[0]*100:.2f}%)")
    st.write("Made with ❤️ by [Ike-uchendu joy chidera]")
    st.write("Source code: [GitHub](https://github.com/email-security-app/email-security-app)")

    # Run the app
if __name__ == "__main__":
    main()