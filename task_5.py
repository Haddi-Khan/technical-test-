# Task 5:
# Given the list:
# marks = [40, 55, 80, 90, 30]
# Use a list comprehension to extract only the marks that are greater than 50.

marks = [40, 55, 80, 90, 30]

high_marks = [m for m in marks if m > 50]
print(high_marks)