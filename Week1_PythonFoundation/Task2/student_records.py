students = []

def add_student():
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }
    students.append(student)
    print("Student added")

def update_student():
    roll = input("Enter roll number to update: ")
    for student in students:
        if student["roll"] == roll:
            student["marks"] = float(input("Enter new marks: "))
            print("Student updated")
            return
    print("Student not found")

def display_students():
    if not students:
        print("No records available")
    for student in students:
        print(student)

if __name__ == "__main__":
    while True:
        print("\n1 Add Student")
        print("2 Update Student")
        print("3 Display Students")
        print("4 Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            display_students()
        elif choice == "4":
            break
        else:
            print("Invalid choice")
