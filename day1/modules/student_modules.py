from modules.result_calculator import calculate_percentage


student_name = input("Enter student name: ")

marks_python = float(input("Enter Python marks: "))
marks_math = float(input("Enter Mathematics marks: "))
marks_comm = float(input("Enter Communication marks: "))

# TODO:
# Import the calculate_percentage function
# from your module
percentage = calculate_percentage(
 marks_python,
 marks_math,
 marks_comm
)

# TODO:
# Calculate the percentage using the imported function

percentage = 0
print("\n--- Result ---")
print(f"Student: {student_name}")
print(f"Percentage: {percentage}")
