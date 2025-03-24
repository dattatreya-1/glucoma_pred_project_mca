import streamlit as st
import pandas as pd
import xgboost as xgb

# Load the saved XGBoost model
model = xgb.XGBClassifier()
model.load_model("glucoma_prediction.json")

st.set_page_config(page_title="Glaucoma Prediction App", layout="centered")

st.title("🧠 Glaucoma Prediction App")
st.markdown("""
This app predicts the likelihood of **Glaucoma** based on patient EHR data (OS - Left Eye).

Please input the values below and click **Predict** to see the result.
""")

# User Input Section
def user_input_features():
    age = st.number_input("Age", min_value=15, max_value=90, value=62)
    gender = st.selectbox("Gender", options=[0, 1], format_func=lambda x: "Male" if x == 0 else "Female")
    dioptre_1 = st.number_input("Dioptre 1", min_value=-8.0, max_value=11.25, value=0.75)
    dioptre_2 = st.number_input("Dioptre 2", min_value=-4.0, max_value=2.0, value=-0.75)
    astigmatism = st.number_input("Astigmatism", min_value=0.0, max_value=180.0, value=90.0)
    phakic = st.selectbox("Phakic / Pseudophakic", options=[0, 1], format_func=lambda x: "Phakic" if x == 0 else "Pseudophakic")
    pneumatic = st.number_input("Pneumatic Pressure", min_value=9.0, max_value=29.0, value=16.0)
    pachymetry = st.number_input("Pachymetry (Corneal Thickness)", min_value=421.0, max_value=648.0, value=535.0)
    axial_length = st.number_input("Axial Length", min_value=21.05, max_value=27.97, value=23.39)

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

    features = pd.DataFrame([data])
    return features

input_df = user_input_features()

# Predict on button click
if st.button("🔍 Predict"):
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)

    class_map = {
        0: "Healthy",
        1: "Early Glaucoma",
        2: "Moderate/Severe Glaucoma"
    }

    predicted_class = prediction[0]
    predicted_label = class_map[predicted_class]

    st.success(f"🧾 **Predicted Diagnosis:** {predicted_label}")

    st.subheader("📊 Prediction Confidence")
    for i in range(len(class_map)):
        st.write(f"{class_map[i]}: {prediction_proba[0][i]*100:.2f}%")
