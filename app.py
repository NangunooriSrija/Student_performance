
import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="wide"
)

# Load trained model
model = joblib.load("student_model.pkl")

# Application title
st.title("🎓 Student Performance Prediction")
st.write("Predict student math performance using academic and personal details.")

st.divider()

# Input fields
st.subheader("Enter Student Details")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox(
        "Gender",
        ["female", "male"]
    )

    race = st.selectbox(
        "Race/Ethnicity",
        ["group A", "group B", "group C", "group D", "group E"]
    )

    parental_education = st.selectbox(
        "Parental Level of Education",
        [
            "some high school",
            "high school",
            "some college",
            "associate's degree",
            "bachelor's degree",
            "master's degree"
        ]
    )

    lunch = st.selectbox(
        "Lunch",
        ["standard", "free/reduced"]
    )

with col2:
    test_prep = st.selectbox(
        "Test Preparation Course",
        ["none", "completed"]
    )

    reading_score = st.number_input(
        "Reading Score",
        min_value=0,
        max_value=100,
        value=70
    )

    writing_score = st.number_input(
        "Writing Score",
        min_value=0,
        max_value=100,
        value=70
    )

st.divider()

# Prediction
if st.button("Predict Math Score", type="primary"):

    input_data = pd.DataFrame({
        "gender": [gender],
        "race/ethnicity": [race],
        "parental level of education": [parental_education],
        "lunch": [lunch],
        "test preparation course": [test_prep],
        "reading score": [reading_score],
        "writing score": [writing_score]
    })

    prediction = model.predict(input_data)

    predicted_score = float(prediction[0])

    st.subheader("Prediction Result")

    st.metric(
        label="Predicted Math Score",
        value=f"{predicted_score:.2f} / 100"
    )

    if predicted_score >= 75:
        st.success("Excellent performance!")
    elif predicted_score >= 50:
        st.info("Good performance. There is room for improvement.")
    else:
        st.warning("The student may need additional academic support.")
