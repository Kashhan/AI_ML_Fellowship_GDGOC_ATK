import streamlit as st
import json
import os



# OOP MODEL

class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course
        }



# FILE HANDLING

DATA_FILE = "students.json"


def load_students():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_students(students):
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)



# STREAMLIT UI

st.set_page_config(page_title="Student Management App")

st.title("Student Management App")

menu = st.sidebar.selectbox(
    "Menu",
    ["Add Student", "View Students"]
)



# ADD STUDENT

if menu == "Add Student":
    st.subheader("Add New Student")

    student_id = st.text_input("Student ID")
    name = st.text_input("Student Name")
    age = st.number_input("Age", min_value=1, max_value=100)
    course = st.text_input("Course")

    if st.button("Save Student"):
        if not student_id or not name or not course:
            st.error("All fields are required")
        else:
            students = load_students()
            new_student = Student(student_id, name, age, course)
            students.append(new_student.to_dict())
            save_students(students)
            st.success("Student added successfully")



# VIEW STUDENTS

elif menu == "View Students":
    st.subheader("Student Records")

    students = load_students()

    if len(students) == 0:
        st.info("No student records found")
    else:
        st.table(students)
