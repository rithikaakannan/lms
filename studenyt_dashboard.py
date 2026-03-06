import streamlit as st
import pandas as pd
import plotly.express as px

def student_dashboard():

    st.header("Student Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Attendance", "85%")
    col2.metric("Assignments", "3 Pending")
    col3.metric("Course Progress", "70%")

    data = pd.DataFrame({
        "Week": ["W1", "W2", "W3", "W4"],
        "Attendance": [80, 85, 90, 88]
    })

    fig = px.line(data, x="Week", y="Attendance", title="Attendance Trend")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Notifications")

    st.info("New Assignment Uploaded")
