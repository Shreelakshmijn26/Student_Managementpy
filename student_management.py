import json
import os

# File to store student data
STUDENT_DATA_FILE = "Students_Jensen.json"

class Student:
    def __init__(self, id, name, age, grade, subjects):
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = subjects

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
            "subjects": self.subjects
        }

# Load students from the file
def load_students_from_file():
    if not os.path.exists(STUDENT_DATA_FILE):
        return []
    try:
        with open(STUDENT_DATA_FILE, "r") as file:
            return [Student(**data) for data in json.load(file)]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save students to the file
def save_students_to_file(students):
    with open(STUDENT_DATA_FILE, "w") as file:
        json.dump([student.to_dict() for student in students], file, indent=4)

# Add a new student
def add_student(name, age, grade, student_id, address):
    students = load_students_from_file()
    try:
        student_id = int(input("Enter ID: "))
        if any(student.id == student_id for student in students):
            print("ID already exists. Try again.")
            return
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = input("Enter grade (e.g., VG, G): ")
        subjects = input("Enter subjects (comma-separated): ").split(",")
        students.append(Student(student_id, name, age, grade, [s.strip() for s in subjects]))
        save_students_to_file(students)
        print("Student added successfully!")
    except ValueError:
        print("Invalid input. Please enter valid data.")

# View all students
def view_students():
    students = load_students_from_file()
    if not students:
        print("No students found.")
        return
    for student in students:
        print(f"ID: {student.id}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}, Subjects: {', '.join(student.subjects)}")

# Update a student's information
def update_student():
    students = load_students_from_file()
    try:
        student_id = int(input("Enter the ID of the student to update: "))
        student = next((s for s in students if s.id == student_id), None)
        if not student:
            print("Student not found.")
            return
        student.name = input(f"Enter new name ({student.name}): ") or student.name
        student.age = int(input(f"Enter new age ({student.age}): ") or student.age)
        student.grade = input(f"Enter new grade ({student.grade}): ") or student.grade
        subjects = input(f"Enter new subjects (comma-separated) ({', '.join(student.subjects)}): ")
        student.subjects = [s.strip() for s in subjects.split(",")] if subjects else student.subjects
        save_students_to_file(students)
        print("Student updated successfully!")
    except ValueError:
        print("Invalid input. Update failed.")

# Delete a student
def delete_student():
    students = load_students_from_file()
    try:
        student_id = int(input("Enter the ID of the student to delete: "))
        students = [s for s in students if s.id != student_id]
        save_students_to_file(students)
        print("Student deleted successfully!")
    except ValueError:
        print("Invalid input. Deletion failed.")

# Main menu
def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
