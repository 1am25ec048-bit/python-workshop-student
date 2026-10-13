
import json


def save_students(students, filename):
    """Save students to a JSON file."""

    data = []

    for student in students:
        data.append({
            "name": student.name,
            "age": student.age,
            "python": student.python,
            "mathematics": student.mathematics,
            "communication": student.communication
        })

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_students(filename, student_class):
    """Load students from a JSON file."""

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("Error: Student data must be a JSON list.")
            return []

        students = []

        for student_data in data:
            try:
                student = student_class(
                    student_data["name"],
                    int(student_data["age"]),
                    float(student_data["python"]),
                    float(student_data["mathematics"]),
                    float(student_data["communication"])
                )

                students.append(student)

            except (KeyError, TypeError, ValueError) as error:
                print(f"Skipping invalid student record: {error}")

        return students

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Error: Invalid JSON file.")
        return []
