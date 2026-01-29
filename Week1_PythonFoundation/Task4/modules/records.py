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
        return

    for student in students:
        print(student)

def student_menu():
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


FILE_NAME = "contacts.txt"

def add_contact(name, phone):
    try:
        with open(FILE_NAME, "a") as file:
            file.write(f"{name},{phone}\n")
        print("Contact saved successfully")
    except Exception as e:
        print("Error saving contact:", e)

def view_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("No contacts found")
                return

            for contact in contacts:
                name, phone = contact.strip().split(",")
                print(f"Name: {name}, Phone: {phone}")
    except FileNotFoundError:
        print("Contact file does not exist")

def update_contact(name, new_phone):
    try:
        updated = False
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()

        with open(FILE_NAME, "w") as file:
            for contact in contacts:
                old_name, phone = contact.strip().split(",")
                if old_name == name:
                    file.write(f"{name},{new_phone}\n")
                    updated = True
                else:
                    file.write(contact)

        if updated:
            print("Contact updated")
        else:
            print("Contact not found")

    except FileNotFoundError:
        print("Contact file not found")

def contact_menu():
    while True:
        print("\n1 Add Contact")
        print("2 View Contacts")
        print("3 Update Contact")
        print("4 Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            add_contact(name, phone)

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            name = input("Enter name to update: ")
            phone = input("Enter new phone: ")
            update_contact(name, phone)

        elif choice == "4":
            break
        else:
            print("Invalid choice")
