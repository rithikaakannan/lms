import streamlit as st
from data import assignments

def assignment_page():

    st.header("Assignments")

    st.dataframe(assignments)

    st.subheader("Upload Assignment")

    title = st.text_input("Assignment Title")
    date = st.date_input("Due Date")

    if st.button("Add Assignment"):

        st.success("Assignment Added")
