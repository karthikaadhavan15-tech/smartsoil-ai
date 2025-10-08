import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("soil_strength_model.pkl")

# App title and intro
st.set_page_config(page_title="SmartSoil AI", page_icon="🌱", layout="centered")
st.title("🌱 SmartSoil AI – Soil Strength Predictor")
st.markdown("""
#### Predict Soil Bearing Capacity / CBR using AI  
This tool uses a trained Random Forest model to estimate soil strength based on basic soil properties.
""")

# Input fields
col1, col2 = st.columns(2)
with col1:
    moisture = st.number_input("Moisture Content (%)", 0.0, 50.0, 10.0)
    density = st.number_input("Dry Density (g/cc)", 1.0, 2.5, 1.8)
with col2:
    PI = st.number_input("Plasticity Index (%)", 0.0, 50.0, 10.0)
    SPT = st.number_input("SPT Value (N)", 0.0, 100.0, 15.0)

# Predict button
if st.button("🔍 Predict Strength"):
    features = np.array([[moisture, density, PI, SPT]])
    result = model.predict(features)[0]
    st.success(f"**Predicted CBR Value:** {result:.2f}")
    st.progress(min(result / 15, 1.0))
    
    if result < 5:
        st.warning("🟠 Weak soil – may need stabilization.")
    elif 5 <= result < 8:
        st.info("🟡 Medium strength soil – suitable for subgrade S2.")
    else:
        st.success("🟢 Strong soil – good bearing capacity.")

# Footer
st.markdown("---")
st.markdown("**Developed by:** Civitas | AI for Civil Engineering 💻")