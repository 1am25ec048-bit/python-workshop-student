
class Student:
    """Represent a student."""

    def __init__(self, name, age, python, mathematics, communication):
        """Initialize student details."""
        self.name = name
        self.age = age
        self.python = float(python)
        self.mathematics = float(mathematics)
        self.communication = float(communication)

    def calculate_percentage(self):
        """Calculate the student's percentage."""
        total = (
            self.python
            + self.mathematics
            + self.communication
        )

        percentage = total / 3
        return percentage

    def display(self):
        """Display the student's details."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Python: {self.python:.2f}")
        print(f"Mathematics: {self.mathematics:.2f}")
        print(f"Communication: {self.communication:.2f}")
        print(
            f"Percentage: "
            f"{self.calculate_percentage():.2f}%"
        )
