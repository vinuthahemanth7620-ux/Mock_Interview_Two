
class Student:
    def __init__(self, name, age, marks):
        if age <= 0:
            raise ValueError("Age must be greater than 0")

        if marks < 0 or marks > 700:
            raise ValueError("Marks must be between 0 and 700")

        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Total Marks:", self.marks)

    def calculate(self):
        if self.marks >= 600:
            print("Grade: A")
            return "Pass"
        elif self.marks >= 400:
            print("Grade: B")
            return "Pass"
        else:
            print("Result: Failed")
            return "Fail"


try:
    n = int(input("Enter number of students: "))

    if n <= 0:
        raise ValueError("Number of students must be greater than 0")

    students = []
    passed = 0
    failed = 0

    for i in range(n):
        print("\nEnter details for Student", i + 1)

        name = input("Enter name: ")
        age = int(input("Enter age: "))
        marks = int(input("Enter total marks (0-700): "))

        student = Student(name, age, marks)
        students.append(student)

    print("\n========== STUDENT RESULTS ==========")

    for student in students:
        print("-----------------------------------")
        student.display()
        result = student.calculate()

        if result == "Pass":
            passed += 1
        else:
            failed += 1

    print("-----------------------------------")
    print("Total Students:", n)
    print("Students Passed:", passed)
    print("Students Failed:", failed)

except ValueError as e:
    print("Error:", e)
