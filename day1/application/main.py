from student import Student
from student_manager import StudentManager
from storage import load_students, save_students

manager = StudentManager()

# Load students from students.json
students = load_students()

for student in students:
    manager.add_student(student)


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Find Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Read student details
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        marks = float(input("Enter student marks: "))

        # Create Student object
        student = Student(name, age, marks)

        # Add student
        manager.add_student(student)

        # Save students
        save_students(manager.students)

        print("Student added successfully.")

    elif choice == "2":
        # View students
        students = manager.view_students()

        if students:
            for student in students:
                print(student)
        else:
            print("No students found.")

    elif choice == "3":
        # Read a name
        name = input("Enter student name: ")

        # Find the student
        student = manager.find_student(name)

        # Display the student if found
        if student:
            print(student)
        else:
            print("Student not found.")

    elif choice == "4":
        # Read student name and new marks
        name = input("Enter student name: ")
        new_marks = float(input("Enter new marks: "))

        # Update student
        if manager.update_student(name, new_marks):
            save_students(manager.students)
            print("Student updated successfully.")
        else:
            print("Student not found.")

    elif choice == "5":
        # Read student name
        name = input("Enter student name: ")

        # Delete student
        if manager.delete_student(name):
            save_students(manager.students)
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    elif choice == "6":
        print("Exiting application.")
        break

    else:
        print("Invalid choice.")
