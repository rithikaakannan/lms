import streamlit as st
import pandas as pd
import plotly.express as px

def faculty_dashboard():

    st.header("Faculty Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Students", "120")
    col2.metric("Assignments Submitted", "85")
    col3.metric("Classes Conducted", "30")

    data = pd.DataFrame({
        "Students": ["A", "B", "C", "D"],
        "Marks": [80, 65, 90, 75]
    })

    fig = px.bar(data, x="Students", y="Marks", title="Student Performance")

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Announcements")

    st.success("Mid Term Exams Next Week")
