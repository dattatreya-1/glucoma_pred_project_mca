# 🧠 Glaucoma Prediction App

This is a simple and interactive **Streamlit web app** that predicts the likelihood of Glaucoma using a trained XGBoost model based on patient EHR (Electronic Health Record) data for the **left eye (OS)**.

## 🚀 Live App

👉 [Click here to access the app](https://glucomapredprojectmca-jmszyprjevwwd8balptmzd.streamlit.app/)
*(Replace the above URL with your actual Streamlit Cloud URL once deployed)*

---

## 📋 Features

- User-friendly interface to input patient details
- Predicts if the eye is:
  - ✅ Healthy
  - 🟡 Early Glaucoma
  - 🔴 Moderate/Severe Glaucoma
- Displays class prediction and confidence scores

---

## 🧾 Input Fields

| Feature                 | Description                             | Range        |
|-------------------------|-----------------------------------------|--------------|
| Age                    | Patient age                              | 15 - 90      |
| Gender                 | 0 = Male, 1 = Female                     | 0 or 1       |
| Dioptre 1              | First dioptre value                      | -8.0 to 11.25|
| Dioptre 2              | Second dioptre value                     | -4.0 to 2.0  |
| Astigmatism            | Degree of astigmatism                    | 0 - 180      |
| Phakic/Pseudophakic    | 0 = Phakic, 1 = Pseudophakic             | 0 or 1       |
| Pneumatic Pressure     | Eye pressure (Pneumatic)                 | 9 - 29       |
| Pachymetry             | Corneal thickness                        | 421 - 648    |
| Axial Length           | Length of the eyeball                    | 21.05 - 27.97|

---

## 🧠 Model Details

- **Algorithm**: XGBoost Classifier  
- **Training Data**: EHR records for left eye (OS)  
- **Target Classes**:
  - `0`: Healthy  
  - `1`: Early Glaucoma  
  - `2`: Moderate/Severe Glaucoma

---

## 🛠️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/glaucoma-predictor.git
cd glaucoma-predictor

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
