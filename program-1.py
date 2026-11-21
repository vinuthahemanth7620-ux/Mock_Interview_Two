class Employee:
    def __init__(self, emp_id, name, age, salary):
        if emp_id <= 0:
            raise ValueError("Employee ID must be greater than 0")

        if not name.strip() or not name.replace(" ", "").isalpha():
            raise ValueError("Name must contain only alphabets and spaces")

        if age < 18:
            raise ValueError("Employee Age must be at least 18")

        if salary <= 6000:
            raise ValueError("Salary must be greater than 6000")

        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print("\n--- Employee Details ---")
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.name)
        print("Employee Age:", self.age)
        print("Employee Salary: Rs.", self.salary)


try:
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    salary = float(input("Enter Employee Salary: "))

    emp = Employee(emp_id, name, age, salary)
    emp.display()

except ValueError as e:
    print("Error:", e)
