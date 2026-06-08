# Create a dictionary of student names and marks, then find the student with the highest marks.

marks = {
    "Rahul": 85,
    "Amit": 92,
    "Priya": 88,
    "Sneha": 95
}

top_student = max(marks, key=marks.get)

print("Student with highest marks:", top_student)
print("Marks:", marks[top_student])
