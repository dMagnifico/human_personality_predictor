import streamlit as st
import joblib
import numpy as np

# Load your trained model (ensure personality_model.pkl is in the same folder)
model = joblib.load('personality_model.pkl')

# Map encoded personality labels back to names
personality_map = {0: "Extrovert", 1: "Introvert"}

# Page title
st.title("🧠 Personality Prediction App")

st.markdown("""
Welcome! Answer the following questions about your behavior, and this app will predict your personality type based on your responses.
""")

# 1. Time spent alone
time_spent_alone = st.slider(
    "1. On average, how many hours per day do you spend alone?",
    min_value=0, max_value=10, value=5, step=1
)

# 2. Stage fear
stage_fear = st.selectbox(
    "2. Do you experience stage fear when speaking in front of people?",
    options=["No", "Yes"]
)

# 3. Social event attendance
social_event_attendance = st.slider(
    "3. How often do you attend social events? (0 = Never, 10 = Very Frequently)",
    min_value=0, max_value=10, value=5, step=1
)

# 4. Going outside
going_outside = st.slider(
    "4. How often do you go outside? (0 = Never, 10 = Every day or very often)",
    min_value=0, max_value=10, value=5, step=1
)

# 5. Drained after socializing
drained_after_socializing = st.selectbox(
    "5. Do you feel mentally or physically drained after socializing?",
    options=["No", "Yes"]
)

# 6. Friends circle size
friends_circle_size = st.slider(
    "6. How many close friends do you have? (Estimate from 0 to 10)",
    min_value=0, max_value=10, value=5, step=1
)

# 7. Post frequency
post_frequency = st.slider(
    "7. How often do you post on social media? (0 = Never, 10 = Very Frequently)",
    min_value=0, max_value=10, value=5, step=1
)

# Convert Yes/No to numeric encoding
stage_fear_encoded = 1 if stage_fear == "Yes" else 0
drained_after_socializing_encoded = 1 if drained_after_socializing == "Yes" else 0

# Predict button
if st.button("🎯 Predict Personality"):

    # Prepare input data
    input_data = np.array([[
        time_spent_alone,
        stage_fear_encoded,
        social_event_attendance,
        going_outside,
        drained_after_socializing_encoded,
        friends_circle_size,
        post_frequency
    ]])

    # Make prediction
    prediction_encoded = model.predict(input_data)[0]
    personality = personality_map.get(prediction_encoded, "Unknown")

    # Show result
    st.success(f"🧬 Predicted Personality: **{personality}**")
