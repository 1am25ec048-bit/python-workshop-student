# TODO
# Create a function called calculate_percentage()
mark1 = float(input("Enter first mark: "))
mark2 = float(input("Enter second mark: "))
mark3 = float(input("Enter third mark: "))
def calculate_percentage(mark1, mark2, mark3):
 total = mark1 + mark2 + mark3
 percentage = total / 3
 return percentage
percentage = calculate_percentage(mark1, mark2, mark3)
print("This is the percentage:", percentage)
# It should :
# 1. Accept three marks
# 2. Calculate the total
# 3. Calculate the percentage
# 4. Return the percentage

