import streamlit as st
import re

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔴 Password should be at least 8 characters long.")
    
    # Check uppercase and lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🟠 Include both uppercase and lowercase letters.")
    
    # Check digits
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🟡 Include at least one digit (0-9).")
    
    # Check special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("🟢 Include at least one special character (!@#$%^&*).")
    
    return score, feedback

def main():
    st.set_page_config(page_title="Password Strength Checker", page_icon="🔐", layout="centered")

    # Apply Global CSS using HTML
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
            
            body {
                font-family: 'Poppins', sans-serif;
                background: linear-gradient(135deg, #ff7e5f, #feb47b);
                color: #ecf0f1;
            }
            .big-font { font-size: 20px !important; font-weight: bold; text-align: center; }
            .success { color: #2ecc71; font-size: 18px; font-weight: bold; }
            .warning { color: #f39c12; font-size: 18px; font-weight: bold; }
            .error { color: #e74c3c; font-size: 18px; font-weight: bold; }
            .container {
                text-align: center;
                padding: 20px;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 10px;
                margin-top: 20px;
                box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.2);
            }
            input[type="password"] {
                background-color: #171717;
                color: white;
                padding: 8px;
                border-radius: 5px;
                border: none;
                width: 100%;
            }
            .st-emotion-cache-bm2z3a{
                    background: linear-gradient(135deg, #e0eafc, #cfdef3); 
                }
                
        </style>
    """, unsafe_allow_html=True)

    st.title("🔐 Password Strength Checker")
    st.write("Enter a password to check its strength and get suggestions for improvement.")

    # Centered container
    st.markdown('<div class="container">', unsafe_allow_html=True)

    password = st.text_input("🔑 Enter your password:", type="password")

    if password:
        score, feedback = check_password_strength(password)

        if score <= 2:
            st.markdown('<p class="error">❌ Weak Password</p>', unsafe_allow_html=True)
        elif score == 3 or score == 4:
            st.markdown('<p class="warning">⚠️ Moderate Password</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="success">✅ Strong Password</p>', unsafe_allow_html=True)

        if feedback:
            st.write("### 🔧 Suggestions to Improve Your Password:")
            for tip in feedback:
                st.write(f"- {tip}")

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
