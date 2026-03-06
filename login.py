import streamlit as st
from data import students, faculty

def login():

    st.title("CLMS Login Portal")

    role = st.radio("Login As", ["Student", "Faculty"])

    user_id = st.text_input("User ID")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if role == "Student":
            if user_id in students and students[user_id] == password:
                st.session_state["login"] = True
                st.session_state["role"] = "student"
                st.success("Login Successful")

            else:
                st.error("Invalid Student Login")

        if role == "Faculty":
            if user_id in faculty and faculty[user_id] == password:
                st.session_state["login"] = True
                st.session_state["role"] = "faculty"
                st.success("Login Successful")

            else:
                st.error("Invalid Faculty Login")
