
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
model = joblib.load("student_performance_model.pkl")

# Application title
st.title("🎓 Student Performance Prediction")
st.write("Predict whether a student will Pass or Fail based on academic and personal details.")

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
if st.button("Predict Result", type="primary"):

    # Create input DataFrame
    input_data = pd.DataFrame({
        "gender": [gender],
        "race/ethnicity": [race],
        "parental level of education": [parental_education],
        "lunch": [lunch],
        "test preparation course": [test_prep],
        "reading score": [reading_score],
        "writing score": [writing_score]
    })

    # Make prediction
    prediction = model.predict(input_data)

    predicted_result = prediction[0]

    # Display result
    st.subheader("Prediction Result")

    if predicted_result == "Pass":
        st.success("🎉 Student Result: PASS")
    else:
        st.error("Student Result: FAIL")

    st.metric(
        label="Predicted Result",
        value=predicted_result
    )
