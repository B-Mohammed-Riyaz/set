import streamlit as st
import pandas as pd
import pickle

# Load the model
model = pickle.load(open('final_model.pkl', 'rb'))

# Streamlit UI
st.title("Career Prediction App")
st.write("Answer the following questions to predict what you might like to become when you grow up:")

# Input fields for questions
q1 = st.radio("Do you like to work with numbers?", ['Yes', 'No'])
q2 = st.radio("Do you enjoy helping others?", ['Yes', 'No'])
q3 = st.radio("Are you interested in technology?", ['Yes', 'No'])
q4 = st.radio("Do you like to lead a team?", ['Yes', 'No'])
q5 = st.radio("Are you good at solving problems?", ['Yes', 'No'])
q6 = st.radio("Do you enjoy creative activities?", ['Yes', 'No'])
q7 = st.radio("Do you prefer working indoors or outdoors?", ['Indoors', 'Outdoors'])
q8 = st.radio("Do you enjoy learning new things?", ['Yes', 'No'])
q9 = st.radio("Do you like to work independently?", ['Yes', 'No'])
q10 = st.radio("Are you comfortable speaking in front of a group?", ['Yes', 'No'])

# Convert answers to binary features or appropriate format
def convert_to_numeric(ans):
    return 1 if ans == 'Yes' else 0

input_data = pd.DataFrame([{
    'Do you like to work with numbers?': convert_to_numeric(q1),
    'Do you enjoy helping others?': convert_to_numeric(q2),
    'Are you interested in technology?': convert_to_numeric(q3),
    'Do you like to lead a team?': convert_to_numeric(q4),
    'Are you good at solving problems?': convert_to_numeric(q5),
    'Do you enjoy creative activities?': convert_to_numeric(q6),
    'Do you prefer working indoors or outdoors?': 1 if q7 == 'Indoors' else 0,
    'Do you enjoy learning new things?': convert_to_numeric(q8),
    'Do you like to work independently?': convert_to_numeric(q9),
    'Are you comfortable speaking in front of a group?': convert_to_numeric(q10)
}])

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    st.success(f"You might like to become a: **{prediction}**")
