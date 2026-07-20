from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


st.set_page_config(page_title="Crop Recommendation", page_icon="🌾", layout="centered")

MODEL_PATH = Path(__file__).with_name("crop_model (1).pkl")
ENCODER_PATH = Path(__file__).with_name("crop_encoders (1).pkl")
FEATURE_COLUMNS = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]


@st.cache_resource
def load_artifacts():
    model = joblib.load(MODEL_PATH)
    encoder = joblib.load(ENCODER_PATH)
    return model, encoder


def predict_from_pkl(values: dict):
    model, encoder = load_artifacts()
    input_df = pd.DataFrame([values], columns=FEATURE_COLUMNS)
    predicted_label = model.predict(input_df)[0]
    predicted_crop = encoder.inverse_transform([predicted_label])[0]
    return predicted_label, predicted_crop


st.title("🌾 Crop Recommendation App")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        nitrogen = st.number_input("Nitrogen (N)", min_value=0.0, value=90.0, step=1.0)
        phosphorus = st.number_input("Phosphorus (P)", min_value=0.0, value=42.0, step=1.0)
        potassium = st.number_input("Potassium (K)", min_value=0.0, value=43.0, step=1.0)
        temperature = st.number_input("Temperature (°C)", min_value=0.0, value=20.0, step=0.1)

    with col2:
        humidity = st.number_input("Humidity (%)", min_value=0.0, value=82.0, step=0.1)
        ph = st.number_input("pH", min_value=0.0, value=6.5, step=0.1)
        rainfall = st.number_input("Rainfall (mm)", min_value=0.0, value=202.0, step=0.1)

    submitted = st.form_submit_button("Predict Crop")

if submitted:
    values = {
        "N": nitrogen,
        "P": phosphorus,
        "K": potassium,
        "temperature": temperature,
        "humidity": humidity,
        "ph": ph,
        "rainfall": rainfall,
    }

    predicted_label, predicted_crop = predict_from_pkl(values)

    st.success(f"Recommended crop: {predicted_crop}")
    st.info(f"Predicted class: {predicted_label}")
    st.caption("Prediction is generated from the saved pickle artifacts in the project folder.")
