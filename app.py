import streamlit as st
from streamlit_option_menu import option_menu

from login import login
from student_dashboard import student_dashboard
from faculty_dashboard import faculty_dashboard
from attendance import attendance
from assignments import assignment_page

st.set_page_config(page_title="CLMS", layout="wide")

if "login" not in st.session_state:
    st.session_state["login"] = False

if not st.session_state["login"]:
    login()

else:

    with st.sidebar:

        selected = option_menu(
            "CLMS Menu",
            ["Dashboard", "Attendance", "Assignments", "Logout"],
            icons=["speedometer", "calendar", "book", "box-arrow-right"],
            default_index=0
        )

    if selected == "Dashboard":

        if st.session_state["role"] == "student":
            student_dashboard()

        else:
            faculty_dashboard()

    if selected == "Attendance":
        attendance()

    if selected == "Assignments":
        assignment_page()

    if selected == "Logout":
        st.session_state["login"] = False
        st.rerun()
