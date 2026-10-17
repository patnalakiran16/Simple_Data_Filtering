# Simple Data Filtering

# Step 1: Create student records
students = [
    {"name": "Kiran", "age": 23, "department": "MCA", "marks": 85},
    {"name": "Ravi", "age": 22, "department": "MCA", "marks": 90},
    {"name": "Priya", "age": 21, "department": "BCA", "marks": 78},
    {"name": "Suresh", "age": 24, "department": "MCA", "marks": 65},
    {"name": "Anusha", "age": 22, "department": "BCA", "marks": 92}
]

# Step 2: Filter students with marks above 80
high_marks = [
    student for student in students
    if student["marks"] > 80
]

print("Students scoring above 80:")
for student in high_marks:
    print(student)

# Step 3: Filter students belonging to MCA
mca_students = [
    student for student in students
    if student["department"] == "MCA"
]

print("\nMCA Students:")
for student in mca_students:
    print(student)

# Step 4: Filter students aged 22 or above
older_students = [
    student for student in students
    if student["age"] >= 22
]

print("\nStudents aged 22 or above:")
for student in older_students:
    print(student)
