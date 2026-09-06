import pickle
import numpy as np
import streamlit as st

# Load the saved model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🎓 Student Exam Score Predictor")
st.write("Adjust the sliders to predict the student's exam score.")

# Numeric inputs (matching the 4 features)
hours_studied = st.slider("Hours Studied per Day", 0.0, 12.0, 5.0, 0.5)
previous_score = st.number_input(
    "Previous Exam Score (0-100)", min_value=0, max_value=100, value=75
)
sleep_hours = st.slider("Sleep Hours per Night", 4.0, 10.0, 7.0, 0.5)
sample_papers = st.slider(
    "Sample Papers Practiced", min_value=0, max_value=10, value=3
)

if st.button("Predict Exam Score"):
    features = np.array(
        [[hours_studied, previous_score, sleep_hours, sample_papers]]
    )
    prediction = model.predict(features)
    st.success(f"Predicted Final Exam Score: **{prediction[0]:.2f} / 100**")