import streamlit as st
import pandas as pd
import pickle
from datetime import datetime
import os


# Load model

with open(r"C:\Users\BHARATHWAJ\knnml.pkl","rb") as f:

    model = pickle.load(f)



st.set_page_config(
    page_title="Student AI",
    page_icon="🎓",
    layout="wide"
)



st.title(
    "🎓 Student Performance Prediction System"
)



st.sidebar.title(
    "Menu"
)

page = st.sidebar.selectbox(
    "Choose",
    [
        "Prediction",
        "History"
    ]
)



if page=="Prediction":


    st.header(
        "Enter Student Details"
    )


    name = st.text_input(
        "Student Name"
    )


    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female"
        ]
    )


    parent = st.selectbox(
        "Parent Education",
        [
            "School",
            "College",
            "Graduate"
        ]
    )


    income = st.selectbox(
        "Family Income",
        [
            "Low",
            "Medium",
            "High"
        ]
    )


    internet = st.selectbox(
        "Internet Access",
        [
            "Yes",
            "No"
        ]
    )


    preparation = st.selectbox(
        "Test Preparation",
        [
            "Completed",
            "Not Completed"
        ]
    )


    extra = st.selectbox(
        "Extracurricular",
        [
            "Yes",
            "No"
        ]
    )



    math = st.number_input(
        "Math Score",
        0,
        100
    )

    reading = st.number_input(
        "Reading Score",
        0,
        100
    )

    writing = st.number_input(
        "Writing Score",
        0,
        100
    )

    science = st.number_input(
        "Science Score",
        0,
        100
    )

    english = st.number_input(
        "English Score",
        0,
        100
    )

    computer = st.number_input(
        "Computer Score",
        0,
        100
    )

    assignment = st.number_input(
        "Assignment Score",
        0,
        100
    )



    if st.button(
        "Predict"
    ):


        input_data = pd.DataFrame({

        "Gender":[gender],
        "Parent_Education":[parent],
        "Family_Income":[income],
        "Internet_Access":[internet],
        "Test_Preparation":[preparation],
        "Extracurricular":[extra],

        "Math_Score":[math],
        "Reading_Score":[reading],
        "Writing_Score":[writing],
        "Science_Score":[science],
        "English_Score":[english],
        "Computer_Score":[computer],
        "Assignment_Score":[assignment]

        })

        result = model.predict(input_data)[0]

        probability = model.predict_proba(input_data)[0]

        if result==0:

            output="PASS"

        else:

            output="FAIL"



        st.success(
            output
        )


        st.info(
            f"Confidence: {max(probability)*100:.2f}%"
        )



        # Save result

        input_data["Name"]=name

        input_data["Prediction"]=output

        input_data["Time"]=datetime.now()



        file="prediction_history.xlsx"



        if os.path.exists(file):

            old=pd.read_excel(file)

            input_data=pd.concat(
                [
                old,
                input_data
                ]
            )


        input_data.to_excel(
            file,
            index=False
        )



elif page=="History":


    if os.path.exists(
        "prediction_history.xlsx"
    ):

        df=pd.read_excel(
            "prediction_history.xlsx"
        )

        st.dataframe(df)
