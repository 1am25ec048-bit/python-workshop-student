
class StudentManager:
    """Manage a collection of students."""

    def __init__(self):
        """Initialize an empty list of students."""
        self.students = []

    def add_student(self, student):
        """Add a student to the collection."""
        self.students.append(student)
        return True

    def view_students(self):
        """Display all students."""
        if not self.students:
            print("\nNo students found.")
            return

        print("\n===== Student Records =====")

        for student in self.students:
            student.display()
            print("--------------------")

    def find_student(self, name):
        """Find a student by name."""
        for student in self.students:
            if student.name.strip().lower() == name.strip().lower():
                return student

        return None

    def update_student(self, name, python, mathematics, communication):
        """Update marks for an existing student."""
        student = self.find_student(name)

        if student is None:
            return False

        student.python = python
        student.mathematics = mathematics
        student.communication = communication

        # Recalculate percentage after updating marks.
        student.percentage = (
            python + mathematics + communication
        ) / 3

        return True

    def delete_student(self, name):
        """Delete a student by name."""
        student = self.find_student(name)

        if student is None:
            return False

        self.students.remove(student)
        return True


