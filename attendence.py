import streamlit as st
from data import attendance_data

def attendance():

    st.header("Attendance")

    st.dataframe(attendance_data)

    student = st.selectbox("Select Student", attendance_data["Student"])

    present = st.checkbox("Mark Present")

    if st.button("Submit Attendance"):

        if present:
            st.success(f"{student} marked present")
        else:
            st.warning(f"{student} marked absent")
