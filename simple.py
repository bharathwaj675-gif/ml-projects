import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
from io import BytesIO


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Student Performance Management System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CONSTANTS
# ============================================================

SUBJECTS = [
    "Mathematics",
    "Reading",
    "Writing",
    "Science",
    "English",
    "Computer",
    "Assignment"
]


# ============================================================
# DARK EDUCATION THEME
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       MAIN DARK EDUCATION BACKGROUND
       ======================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(37, 99, 235, 0.16),
                transparent 28%
            ),
            radial-gradient(
                circle at 90% 15%,
                rgba(16, 185, 129, 0.12),
                transparent 30%
            ),
            radial-gradient(
                circle at 50% 100%,
                rgba(245, 158, 11, 0.08),
                transparent 35%
            ),
            linear-gradient(
                135deg,
                #07111F 0%,
                #0B1728 45%,
                #0F1F35 100%
            );

        color: #F8FAFC;
    }


    /* ========================================================
       MAIN CONTENT
       ======================================================== */

    .main .block-container {
        max-width: 1400px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }


    /* ========================================================
       HEADINGS
       ======================================================== */

    .main h1 {
        color: #FFFFFF !important;
        font-weight: 800 !important;
        letter-spacing: 0.3px;
    }

    .main h2 {
        color: #60A5FA !important;
        font-weight: 750 !important;
    }

    .main h3 {
        color: #34D399 !important;
        font-weight: 700 !important;
    }

    .main h4 {
        color: #FBBF24 !important;
        font-weight: 700 !important;
    }


    /* ========================================================
       NORMAL TEXT
       ======================================================== */

    .main p {
        color: #D1D5DB !important;
    }

    .main label {
        color: #E5E7EB !important;
    }


    /* ========================================================
       SIDEBAR
       ======================================================== */

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #050B14 0%,
                #0A1628 50%,
                #0B2630 100%
            );

        border-right: 1px solid #1E3A5F;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #FFFFFF !important;
    }

    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] label {
        color: #D1D5DB !important;
    }


    /* ========================================================
       SIDEBAR RADIO
       ======================================================== */

    section[data-testid="stSidebar"]
    div[role="radiogroup"] label {
        background: rgba(30, 58, 95, 0.35);

        border-radius: 9px;

        padding: 8px 12px;

        margin-bottom: 5px;

        transition: 0.2s;
    }

    section[data-testid="stSidebar"]
    div[role="radiogroup"] label:hover {
        background: rgba(37, 99, 235, 0.35);
    }


    /* ========================================================
       TEXT INPUT
       ======================================================== */

    div[data-baseweb="input"] {
        background-color: #111D2E !important;

        border: 1px solid #334155 !important;

        border-radius: 10px;
    }

    div[data-baseweb="input"]:focus-within {
        border: 1px solid #3B82F6 !important;

        box-shadow:
            0 0 0 1px rgba(59, 130, 246, 0.3);
    }

    div[data-baseweb="input"] input {
        background-color: #111D2E !important;

        color: #FFFFFF !important;

        -webkit-text-fill-color: #FFFFFF !important;
    }

    div[data-baseweb="input"] input::placeholder {
        color: #94A3B8 !important;

        -webkit-text-fill-color: #94A3B8 !important;
    }


    /* ========================================================
       NUMBER INPUT
       ======================================================== */

    div[data-testid="stNumberInput"] {
        color: #FFFFFF !important;
    }

    div[data-testid="stNumberInput"] input {
        background-color: #111D2E !important;

        color: #FFFFFF !important;

        -webkit-text-fill-color: #FFFFFF !important;
    }


    /* ========================================================
       TEXT AREA
       ======================================================== */

    textarea {
        background-color: #111D2E !important;

        color: #FFFFFF !important;

        -webkit-text-fill-color: #FFFFFF !important;

        border: 1px solid #334155 !important;

        border-radius: 10px;
    }

    textarea::placeholder {
        color: #94A3B8 !important;

        -webkit-text-fill-color: #94A3B8 !important;
    }


    /* ========================================================
       SELECT BOX
       ======================================================== */

    div[data-baseweb="select"] > div {
        background-color: #111D2E !important;

        color: #FFFFFF !important;

        border: 1px solid #334155 !important;

        border-radius: 10px;
    }

    div[data-baseweb="select"] span {
        color: #FFFFFF !important;
    }


    /* ========================================================
       SELECT DROPDOWN
       ======================================================== */

    ul[role="listbox"] {
        background-color: #111D2E !important;

        border: 1px solid #334155 !important;
    }

    li[role="option"] {
        background-color: #111D2E !important;

        color: #FFFFFF !important;
    }

    li[role="option"]:hover {
        background-color: #1E3A5F !important;
    }


    /* ========================================================
       BUTTONS
       ======================================================== */

    .stButton > button,
    .stFormSubmitButton > button {
        background:
            linear-gradient(
                135deg,
                #2563EB,
                #059669
            ) !important;

        color: #FFFFFF !important;

        border: none !important;

        border-radius: 10px !important;

        padding: 0.65rem 1.3rem !important;

        font-weight: 700 !important;

        box-shadow:
            0 5px 15px rgba(37, 99, 235, 0.25);
    }

    .stButton > button:hover,
    .stFormSubmitButton > button:hover {
        background:
            linear-gradient(
                135deg,
                #1D4ED8,
                #047857
            ) !important;

        color: #FFFFFF !important;

        transform: translateY(-1px);
    }


    /* ========================================================
       METRIC CARDS
       ======================================================== */

    [data-testid="stMetric"] {
        background:
            linear-gradient(
                145deg,
                #111D2E,
                #14243A
            );

        padding: 20px;

        border-radius: 16px;

        border: 1px solid #263B55;

        box-shadow:
            0 8px 25px rgba(0, 0, 0, 0.25);
    }

    [data-testid="stMetric"] label {
        color: #94A3B8 !important;
    }

    [data-testid="stMetricValue"] {
        color: #FFFFFF !important;

        font-weight: 800 !important;
    }


    /* ========================================================
       DATAFRAME
       ======================================================== */

    [data-testid="stDataFrame"] {
        background: #0F1B2D !important;

        border-radius: 14px;

        overflow: hidden;

        border: 1px solid #263B55;
    }


    /* ========================================================
       EXPANDER
       ======================================================== */

    details {
        background: #101D30 !important;

        border: 1px solid #263B55 !important;

        border-radius: 12px !important;
    }

    details summary {
        color: #FFFFFF !important;

        font-weight: 700;
    }


    /* ========================================================
       ALERTS
       ======================================================== */

    div[data-testid="stAlert"][kind="info"] {
        background-color: #0F2742 !important;

        border-left: 5px solid #3B82F6 !important;

        color: #DBEAFE !important;
    }

    div[data-testid="stAlert"][kind="success"] {
        background-color: #0B2B22 !important;

        border-left: 5px solid #10B981 !important;

        color: #D1FAE5 !important;
    }

    div[data-testid="stAlert"][kind="warning"] {
        background-color: #33280B !important;

        border-left: 5px solid #F59E0B !important;

        color: #FEF3C7 !important;
    }

    div[data-testid="stAlert"][kind="error"] {
        background-color: #35151A !important;

        border-left: 5px solid #EF4444 !important;

        color: #FEE2E2 !important;
    }


    /* ========================================================
       DIVIDER
       ======================================================== */

    hr {
        border-color: #263B55 !important;
    }


    /* ========================================================
       CHECKBOX
       ======================================================== */

    div[data-testid="stCheckbox"] label {
        color: #E5E7EB !important;
    }


    /* ========================================================
       TABS
       ======================================================== */

    button[data-baseweb="tab"] {
        color: #CBD5E1 !important;

        font-weight: 600;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        color: #60A5FA !important;
    }


    /* ========================================================
       DOWNLOAD BUTTON
       ======================================================== */

    [data-testid="stDownloadButton"] button {
        background:
            linear-gradient(
                135deg,
                #1E3A8A,
                #047857
            ) !important;

        color: #FFFFFF !important;

        border: none !important;

        border-radius: 10px !important;

        font-weight: 700 !important;
    }


    /* ========================================================
       SCROLLBAR
       ======================================================== */

    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }

    ::-webkit-scrollbar-track {
        background: #07111F;
    }

    ::-webkit-scrollbar-thumb {
        background: #334155;

        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #475569;
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    footer {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

if "student_data" not in st.session_state:
    st.session_state.student_data = None

if "student_records" not in st.session_state:
    st.session_state.student_records = []


# ============================================================
# PERFORMANCE CALCULATION
# ============================================================

def calculate_performance(
    scores,
    attendance,
    study_hours,
    homework
):

    average = round(
        float(np.mean(scores)),
        2
    )

    lowest_score = min(scores)

    # --------------------------------------------------------
    # PASS RULE
    # Every subject must be >= 50
    # AND average must be >= 50
    # --------------------------------------------------------

    if average >= 50 and lowest_score >= 50:
        result = "PASS"
    else:
        result = "FAIL"

    # --------------------------------------------------------
    # RISK LEVEL
    # --------------------------------------------------------

    if result == "FAIL":

        risk_level = "HIGH"

    elif (
        attendance < 75
        or study_hours < 2
        or homework < 75
    ):

        risk_level = "MEDIUM"

    else:

        risk_level = "LOW"

    return average, result, risk_level


# ============================================================
# GET RECORDS
# ============================================================

def get_records_dataframe():

    if len(st.session_state.student_records) == 0:
        return pd.DataFrame()

    return pd.DataFrame(
        st.session_state.student_records
    )


# ============================================================
# DELETE STUDENT
# ============================================================

def delete_student(student_id):

    original_count = len(
        st.session_state.student_records
    )

    st.session_state.student_records = [
        student
        for student in st.session_state.student_records
        if str(
            student.get(
                "Student_ID",
                ""
            )
        ).strip()
        != str(student_id).strip()
    ]

    return (
        len(
            st.session_state.student_records
        )
        < original_count
    )


# ============================================================
# SUBJECT DATA
# ============================================================

def get_subject_data(student):

    return pd.DataFrame(
        {
            "Subject": SUBJECTS,

            "Score": [
                student["Mathematics"],
                student["Reading"],
                student["Writing"],
                student["Science"],
                student["English"],
                student["Computer"],
                student["Assignment"]
            ]
        }
    )


# ============================================================
# EXCEL DOWNLOAD
# ============================================================

def excel_download(df):

    output = BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        df.to_excel(
            writer,
            index=False,
            sheet_name="Students"
        )

    return output.getvalue()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🎓 STUDENT AI")

    st.caption(
        "Performance Intelligence System"
    )

    st.divider()

    page = st.radio(
        "MENU",
        [
            "🏠 Home",
            "👨‍🎓 Student Input",
            "📊 Student Dashboard",
            "👨‍🏫 Teacher Dashboard",
            "⚠️ Early Warning",
            "💡 Personalized Advice",
            "📈 Analytics",
            "📄 Student Report",
            "💾 Student Records"
        ]
    )

    st.divider()

    st.caption(
        "© 2026 Student AI System"
    )


# ============================================================
# MAIN HEADER
# ============================================================

st.title(
    "🎓 Student Performance Management System"
)

st.write(
    "Student Analytics | Performance Monitoring | "
    "Early Warning | Personalized Learning"
)

st.divider()


# ============================================================
# HOME
# ============================================================

if page == "🏠 Home":

    st.header(
        "🚀 Dashboard Overview"
    )

    records = get_records_dataframe()

    total_students = len(records)

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "👨‍🎓 Total Students",
            total_students
        )

    with c2:

        if st.session_state.student_data:

            st.metric(
                "📊 Current Average",
                st.session_state.student_data[
                    "Average"
                ]
            )

        else:

            st.metric(
                "📊 Current Average",
                "No Data"
            )

    with c3:

        if st.session_state.student_data:

            st.metric(
                "🎯 Result",
                st.session_state.student_data[
                    "Result"
                ]
            )

        else:

            st.metric(
                "🎯 Result",
                "No Data"
            )

    with c4:

        if st.session_state.student_data:

            st.metric(
                "⚠️ Risk Level",
                st.session_state.student_data[
                    "Risk_Level"
                ]
            )

        else:

            st.metric(
                "⚠️ Risk Level",
                "No Data"
            )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:

        st.subheader(
            "👨‍🎓 Student Management"
        )

        st.write(
            "Enter student details and "
            "academic performance."
        )

    with col2:

        st.subheader(
            "📊 Smart Analytics"
        )

        st.write(
            "Analyze scores and identify "
            "strong and weak subjects."
        )

    with col3:

        st.subheader(
            "⚠️ Early Warning"
        )

        st.write(
            "Identify students who need "
            "academic improvement."
        )

    st.divider()

    st.subheader(
        "🔄 System Workflow"
    )

    st.info(
        "Student Input → Performance Analysis → "
        "Result → Early Warning → Personalized Advice"
    )


# ============================================================
# STUDENT INPUT
# ============================================================

elif page == "👨‍🎓 Student Input":

    st.header(
        "👨‍🎓 Student Information"
    )

    with st.form(
        "student_form"
    ):

        st.subheader(
            "👤 Basic Information"
        )

        c1, c2, c3 = st.columns(3)

        with c1:

            student_id = st.text_input(
                "Student ID",
                placeholder="Example: ST001"
            )

        with c2:

            student_name = st.text_input(
                "Student Name",
                placeholder="Enter student name"
            )

        with c3:

            gender = st.selectbox(
                "Gender",
                [
                    "Male",
                    "Female",
                    "Other"
                ]
            )

        st.divider()

        st.subheader(
            "📚 Academic Performance"
        )

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            mathematics = st.number_input(
                "Mathematics",
                min_value=0,
                max_value=100,
                value=50
            )

        with c2:

            reading = st.number_input(
                "Reading",
                min_value=0,
                max_value=100,
                value=50
            )

        with c3:

            writing = st.number_input(
                "Writing",
                min_value=0,
                max_value=100,
                value=50
            )

        with c4:

            science = st.number_input(
                "Science",
                min_value=0,
                max_value=100,
                value=50
            )

        c1, c2, c3 = st.columns(3)

        with c1:

            english = st.number_input(
                "English",
                min_value=0,
                max_value=100,
                value=50
            )

        with c2:

            computer = st.number_input(
                "Computer",
                min_value=0,
                max_value=100,
                value=50
            )

        with c3:

            assignment = st.number_input(
                "Assignment",
                min_value=0,
                max_value=100,
                value=50
            )

        st.divider()

        st.subheader(
            "📋 Student Activity"
        )

        c1, c2, c3 = st.columns(3)

        with c1:

            attendance = st.number_input(
                "Attendance (%)",
                min_value=0,
                max_value=100,
                value=75
            )

        with c2:

            study_hours = st.number_input(
                "Study Hours / Day",
                min_value=0.0,
                max_value=24.0,
                value=2.0,
                step=0.5
            )

        with c3:

            homework = st.number_input(
                "Homework Completion (%)",
                min_value=0,
                max_value=100,
                value=75
            )

        submitted = st.form_submit_button(
            "🎯 CALCULATE PERFORMANCE"
        )


    # ========================================================
    # CALCULATE PERFORMANCE
    # ========================================================

    if submitted:

        if student_name.strip() == "":

            st.error(
                "Please enter the student name."
            )

        else:

            scores = [
                mathematics,
                reading,
                writing,
                science,
                english,
                computer,
                assignment
            ]

            average, result, risk_level = (
                calculate_performance(
                    scores,
                    attendance,
                    study_hours,
                    homework
                )
            )

            student = {

                "Student_ID":
                    student_id.strip(),

                "Name":
                    student_name.strip(),

                "Gender":
                    gender,

                "Mathematics":
                    mathematics,

                "Reading":
                    reading,

                "Writing":
                    writing,

                "Science":
                    science,

                "English":
                    english,

                "Computer":
                    computer,

                "Assignment":
                    assignment,

                "Attendance":
                    attendance,

                "Study_Hours":
                    study_hours,

                "Homework":
                    homework,

                "Average":
                    average,

                "Result":
                    result,

                "Risk_Level":
                    risk_level,

                "Created_Date":
                    datetime.now().strftime(
                        "%d-%m-%Y %H:%M:%S"
                    )
            }

            st.session_state.student_data = student

            # ------------------------------------------------
            # ADD OR UPDATE RECORD
            # ------------------------------------------------

            existing_index = None

            for i, old_student in enumerate(
                st.session_state.student_records
            ):

                if (
                    str(
                        old_student.get(
                            "Student_ID",
                            ""
                        )
                    ).strip()
                    ==
                    student_id.strip()
                    and
                    student_id.strip() != ""
                ):

                    existing_index = i

                    break

            if existing_index is not None:

                st.session_state.student_records[
                    existing_index
                ] = student

            else:

                st.session_state.student_records.append(
                    student
                )

            st.success(
                "Performance calculated successfully."
            )

            c1, c2, c3 = st.columns(3)

            with c1:

                st.metric(
                    "Average",
                    average
                )

            with c2:

                st.metric(
                    "Result",
                    result
                )

            with c3:

                st.metric(
                    "Risk Level",
                    risk_level
                )


# ============================================================
# STUDENT DASHBOARD
# ============================================================

elif page == "📊 Student Dashboard":

    if not st.session_state.student_data:

        st.warning(
            "Please enter student information first."
        )

    else:

        student = st.session_state.student_data

        st.header(
            "📊 Student Dashboard"
        )

        st.subheader(
            f"Welcome, {student['Name']} 👋"
        )

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            st.metric(
                "Average",
                student["Average"]
            )

        with c2:

            st.metric(
                "Result",
                student["Result"]
            )

        with c3:

            st.metric(
                "Risk Level",
                student["Risk_Level"]
            )

        with c4:

            st.metric(
                "Attendance",
                f"{student['Attendance']}%"
            )

        subject_data = get_subject_data(
            student
        )

        fig = px.bar(
            subject_data,
            x="Subject",
            y="Score",
            text="Score",
            title="📊 Subject Performance"
        )

        fig.add_hline(
            y=50,
            line_dash="dash",
            annotation_text="Pass Mark"
        )

        fig.update_yaxes(
            range=[0, 100]
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# ============================================================
# TEACHER DASHBOARD
# ============================================================

elif page == "👨‍🏫 Teacher Dashboard":

    st.header(
        "👨‍🏫 Teacher Dashboard"
    )

    records = get_records_dataframe()

    if records.empty:

        st.info(
            "No student records available."
        )

    else:

        total_students = len(records)

        pass_count = (
            records["Result"] == "PASS"
        ).sum()

        fail_count = (
            records["Result"] == "FAIL"
        ).sum()

        pass_rate = round(
            pass_count / total_students * 100,
            2
        )

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            st.metric(
                "Total Students",
                total_students
            )

        with c2:

            st.metric(
                "Passed",
                pass_count
            )

        with c3:

            st.metric(
                "Failed",
                fail_count
            )

        with c4:

            st.metric(
                "Pass Rate",
                f"{pass_rate}%"
            )

        st.dataframe(
            records,
            use_container_width=True,
            hide_index=True
        )


# ============================================================
# EARLY WARNING
# ============================================================

elif page == "⚠️ Early Warning":

    st.header(
        "⚠️ Early Warning System"
    )

    if not st.session_state.student_data:

        st.warning(
            "Please enter student information first."
        )

    else:

        student = st.session_state.student_data

        warnings = []

        subject_data = get_subject_data(
            student
        )

        for _, row in subject_data.iterrows():

            if row["Score"] < 50:

                warnings.append(
                    f"📚 {row['Subject']} score is below 50. "
                    f"Current Score: {row['Score']}"
                )

        if student["Attendance"] < 75:

            warnings.append(
                f"📅 Low Attendance: "
                f"{student['Attendance']}%"
            )

        if student["Study_Hours"] < 2:

            warnings.append(
                f"⏰ Low Study Hours: "
                f"{student['Study_Hours']} hours/day"
            )

        if student["Homework"] < 75:

            warnings.append(
                f"📝 Low Homework Completion: "
                f"{student['Homework']}%"
            )

        if warnings:

            st.error(
                f"Risk Level: {student['Risk_Level']}"
            )

            for warning in warnings:

                st.warning(
                    warning
                )

        else:

            st.success(
                "🎉 No academic warnings detected!"
            )


# ============================================================
# PERSONALIZED ADVICE
# ============================================================

elif page == "💡 Personalized Advice":

    st.header(
        "💡 Personalized Advice"
    )

    if not st.session_state.student_data:

        st.warning(
            "Please enter student information first."
        )

    else:

        student = st.session_state.student_data

        subject_data = get_subject_data(
            student
        )

        advice_found = False

        for _, row in subject_data.iterrows():

            if row["Score"] < 50:

                advice_found = True

                st.info(
                    f"📚 Improve {row['Subject']}. "
                    f"Current Score: {row['Score']}. "
                    f"Target: 50+"
                )

        if student["Attendance"] < 75:

            advice_found = True

            st.info(
                "📅 Improve attendance to 75% or above."
            )

        if student["Study_Hours"] < 2:

            advice_found = True

            st.info(
                "⏰ Increase study time to at least "
                "2 hours per day."
            )

        if student["Homework"] < 75:

            advice_found = True

            st.info(
                "📝 Complete homework more regularly."
            )

        if not advice_found:

            st.success(
                "🌟 Excellent! Continue your current study routine."
            )


# ============================================================
# ANALYTICS
# ============================================================

elif page == "📈 Analytics":

    st.header(
        "📈 Performance Analytics"
    )

    if not st.session_state.student_data:

        st.warning(
            "Please enter student information first."
        )

    else:

        student = st.session_state.student_data

        subject_data = get_subject_data(
            student
        )

        best_subject = subject_data.loc[
            subject_data["Score"].idxmax()
        ]

        weak_subject = subject_data.loc[
            subject_data["Score"].idxmin()
        ]

        passed_subjects = len(
            subject_data[
                subject_data["Score"] >= 50
            ]
        )

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            st.metric(
                "Average",
                student["Average"]
            )

        with c2:

            st.metric(
                "Best Subject",
                best_subject["Subject"]
            )

        with c3:

            st.metric(
                "Weak Subject",
                weak_subject["Subject"]
            )

        with c4:

            st.metric(
                "Subjects Passed",
                f"{passed_subjects}/7"
            )

        fig = px.bar(
            subject_data.sort_values(
                "Score",
                ascending=False
            ),
            x="Score",
            y="Subject",
            orientation="h",
            text="Score",
            title="Subject Comparison"
        )

        fig.add_vline(
            x=50,
            line_dash="dash",
            annotation_text="Pass Mark"
        )

        fig.update_xaxes(
            range=[0, 100]
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# ============================================================
# STUDENT REPORT
# ============================================================

elif page == "📄 Student Report":

    st.header(
        "📄 Student Performance Report"
    )

    if not st.session_state.student_data:

        st.warning(
            "Please enter student information first."
        )

    else:

        student = st.session_state.student_data

        report = f"""
STUDENT PERFORMANCE REPORT
========================================

Student ID: {student['Student_ID']}
Student Name: {student['Name']}
Gender: {student['Gender']}

ACADEMIC PERFORMANCE
========================================

Mathematics: {student['Mathematics']}
Reading: {student['Reading']}
Writing: {student['Writing']}
Science: {student['Science']}
English: {student['English']}
Computer: {student['Computer']}
Assignment: {student['Assignment']}

OVERALL PERFORMANCE
========================================

Average: {student['Average']}
Result: {student['Result']}
Risk Level: {student['Risk_Level']}

STUDENT ACTIVITY
========================================

Attendance: {student['Attendance']}%
Study Hours: {student['Study_Hours']} hours/day
Homework Completion: {student['Homework']}%

Generated:
{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}
"""

        st.text_area(
            "Report Preview",
            report,
            height=500
        )

        st.download_button(
            "⬇️ DOWNLOAD REPORT",
            data=report,
            file_name=f"{student['Name']}_report.txt",
            mime="text/plain"
        )


# ============================================================
# STUDENT RECORDS
# ============================================================

elif page == "💾 Student Records":

    st.header(
        "💾 Student Records"
    )

    records = get_records_dataframe()

    if records.empty:

        st.info(
            "No student records available."
        )

    else:

        c1, c2, c3 = st.columns(3)

        with c1:

            result_filter = st.selectbox(
                "Filter Result",
                [
                    "ALL",
                    "PASS",
                    "FAIL"
                ]
            )

        with c2:

            risk_filter = st.selectbox(
                "Filter Risk Level",
                [
                    "ALL",
                    "LOW",
                    "MEDIUM",
                    "HIGH"
                ]
            )

        with c3:

            search_name = st.text_input(
                "Search Student"
            )

        filtered = records.copy()

        if result_filter != "ALL":

            filtered = filtered[
                filtered["Result"]
                == result_filter
            ]

        if risk_filter != "ALL":

            filtered = filtered[
                filtered["Risk_Level"]
                == risk_filter
            ]

        if search_name:

            filtered = filtered[
                filtered["Name"]
                .astype(str)
                .str.contains(
                    search_name,
                    case=False,
                    na=False
                )
            ]

        st.success(
            f"{len(filtered)} student record(s) found."
        )

        st.dataframe(
            filtered,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        # ====================================================
        # DELETE STUDENT
        # ====================================================

        st.subheader(
            "🗑️ Delete Student Record"
        )

        if not filtered.empty:

            student_options = filtered.apply(
                lambda row:
                f"{row['Student_ID']} - {row['Name']}",
                axis=1
            ).tolist()

            selected_student = st.selectbox(
                "Select Student",
                student_options
            )

            selected_index = student_options.index(
                selected_student
            )

            selected_student_id = filtered.iloc[
                selected_index
            ]["Student_ID"]

            confirm_delete = st.checkbox(
                "I confirm that I want to delete this student."
            )

            if st.button(
                "🗑️ DELETE SELECTED STUDENT",
                use_container_width=True
            ):

                if not confirm_delete:

                    st.error(
                        "Please confirm deletion first."
                    )

                else:

                    success = delete_student(
                        selected_student_id
                    )

                    if success:

                        if (
                            st.session_state.student_data
                            and
                            str(
                                st.session_state.student_data.get(
                                    "Student_ID",
                                    ""
                                )
                            )
                            ==
                            str(selected_student_id)
                        ):

                            st.session_state.student_data = None

                        st.success(
                            "Student deleted successfully."
                        )

                        st.rerun()

                    else:

                        st.error(
                            "Student could not be deleted."
                        )

        else:

            st.info(
                "No students match the selected filters."
            )

        st.divider()

        # ====================================================
        # EXCEL DOWNLOAD
        # ====================================================

        st.subheader(
            "📥 Download Records"
        )

        excel_file = excel_download(
            filtered
        )

        st.download_button(
            "⬇️ DOWNLOAD EXCEL",
            data=excel_file,
            file_name="student_records.xlsx",
            mime=(
                "application/vnd.openxmlformats-officedocument."
                "spreadsheetml.sheet"
            ),
            use_container_width=True
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    "### 🎓 Student Performance Management System"
)

st.caption(
    "Student Performance Intelligence Platform"
)

st.caption(
    "© 2026 Student AI System"
)