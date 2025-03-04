import streamlit as st
import re

st.set_page_config(page_title="Password Strength Meter", layout="centered")
st.title("Password Strength Meter")

requirements = [
    {
        "id": "length",
        "label": "At least 8 characters",
        "validator": lambda password: len(password) >= 8
    },
    {
        "id": "lowercase",
        "label": "At least one lowercase letter",
        "validator": lambda password: bool(re.search(r'[a-z]', password))
    },
    {
        "id": "uppercase",
        "label": "At least one uppercase letter",
        "validator": lambda password: bool(re.search(r'[A-Z]', password))
    },
    {
        "id": "number",
        "label": "At least one number",
        "validator": lambda password: bool(re.search(r'[0-9]', password))
    },
    {
        "id": "special",
        "label": "At least one special character",
        "validator": lambda password: bool(re.search(r'[^A-Za-z0-9]', password))
    }
]

password = st.text_input("Enter your password", type="password")

if password:
    met_requirements = [req for req in requirements if req["validator"](password)]
    strength_score = len(met_requirements) / len(requirements)
    strength_percentage = strength_score * 100
    
    if strength_score == 1:
        feedback = "Strong password"
        color = "green"
    elif strength_score >= 0.6:
        feedback = "Moderate password"
        color = "orange"
    else:
        feedback = "Weak password"
        color = "red"
    
    st.write(f"**Strength:** {feedback}")
    st.progress(strength_percentage / 100)
    
    st.markdown(
        f"""
        <style>
        .stProgress > div > div {{
            background-color: {color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.write("**Requirements:**")
    for req in requirements:
        is_met = req["validator"](password)
        icon = "✅" if is_met else "❌"
        st.markdown(f"{icon} {req['label']}")
else:
    st.write("**Strength:**")
    st.progress(0)
    
    st.write("**Requirements:**")
    for req in requirements:
        st.markdown(f"❌ {req['label']}")

st.markdown("---")
st.markdown("""
### Password Security Tips:
- Use a password manager to store and generate passwords
- Avoid password reuse across websites and apps
- Avoid using personal information in passwords
- Enable Multi-Factor Authentication when available
""")

