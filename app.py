import streamlit as st
import pandas as pd
import xgboost as xgb

# --- Set Page Config ---
st.set_page_config(
    page_title="Glaucoma Prediction App",
    page_icon="🧠",
    layout="centered"
)

# --- Header ---
st.markdown("""
    <h1 style='text-align: center; color: darkblue;'>🧠 Glaucoma Prediction App</h1>
    <p style='text-align: center; font-size: 18px;'>Predict the stage of glaucoma based on patient EHR data (Left Eye - OS).</p>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Load Model ---
model = xgb.XGBClassifier()
model.load_model("glucoma_prediction.json")

# --- Sidebar (optional future use) ---
# st.sidebar.header("Navigation")

# --- Input Layout ---
st.subheader("📥 Enter Patient Data")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("🗓️ Age", min_value=15, max_value=90, value=62)
    gender = st.selectbox("🚻 Gender", options=[0, 1], format_func=lambda x: "Male" if x == 0 else "Female")
    dioptre_1 = st.number_input("👁️ Dioptre 1", min_value=-8.0, max_value=11.25, value=0.75)
    astigmatism = st.number_input("🎯 Astigmatism", min_value=0.0, max_value=180.0, value=90.0)
    pneumatic = st.number_input("💨 Pneumatic Pressure", min_value=9.0, max_value=29.0, value=16.0)

with col2:
    dioptre_2 = st.number_input("👁️ Dioptre 2", min_value=-4.0, max_value=2.0, value=-0.75)
    phakic = st.selectbox("🦴 Lens Type", options=[0, 1], format_func=lambda x: "Phakic" if x == 0 else "Pseudophakic")
    pachymetry = st.number_input("📏 Pachymetry (Thickness)", min_value=421.0, max_value=648.0, value=535.0)
    axial_length = st.number_input("📐 Axial Length", min_value=21.05, max_value=27.97, value=23.39)

# --- Prepare Input Data ---
data = {
    'Age': age,
    'Gender': gender,
    'dioptre_1': dioptre_1,
    'dioptre_2': dioptre_2,
    'astigmatism': astigmatism,
    'Phakic/Pseudophakic': phakic,
    'Pneumatic': pneumatic,
    'Pachymetry': pachymetry,
    'Axial_Length': axial_length
}

input_df = pd.DataFrame([data])

# --- Predict Button ---
st.markdown("---")
if st.button("🔍 Predict"):
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)

    class_map = {
        0: "✅ Healthy",
        1: "🟡 Early Glaucoma",
        2: "🔴 Moderate/Severe Glaucoma"
    }

    predicted_class = prediction[0]
    predicted_label = class_map[predicted_class]

    st.success(f"🧾 **Predicted Diagnosis:** {predicted_label}")

    st.subheader("📊 Prediction Confidence")
    for i in range(len(class_map)):
        st.write(f"{class_map[i]}: **{prediction_proba[0][i]*100:.2f}%**")

# --- Footer ---
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>© 2025 Glaucoma Predictor | Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)
