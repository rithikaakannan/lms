import pandas as pd

# Student Login Data
students = {
    "STU101": "1234",
    "STU102": "1234",
    "STU103": "1234"
}

# Faculty Login Data
faculty = {
    "FAC101": "admin",
    "FAC102": "admin"
}

# Attendance Data
attendance_data = pd.DataFrame({
    "Student": ["STU101", "STU102", "STU103"],
    "Attendance": [85, 78, 92]
})

# Assignment Data
assignments = pd.DataFrame({
    "Title": ["Python Basics", "Data Structures", "Mini Project"],
    "Due Date": ["10 Mar", "15 Mar", "20 Mar"]
})
