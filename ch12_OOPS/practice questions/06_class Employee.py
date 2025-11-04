# Q6. Create a class Employee
# Class Variable: company_name = "TechCorp"
# Instance Variables: name, salary
# Method: display() to show details
# Try: Change the company name from one object and see how it affects others.

class Employee():
    company_name="TechCorp"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display(self):
        print("Company name: ", Employee.company_name)
        print("Name: ",self.name)
        print("Salary: ",self.salary)

emp1 = Employee("Sahana", 50000)
emp2 = Employee("Ravi", 60000)

print("Before changing company name:")
emp1.display()
emp2.display()

# Changing the class variable through the class itself
Employee.company_name = "DataWorks"

print("\nAfter changing company name:")
emp1.display()
emp2.display()




