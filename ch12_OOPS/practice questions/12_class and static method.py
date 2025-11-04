class Employee:
    company = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name   # modifies class variable

    @staticmethod
    def greet():
        print("Welcome to the company!")

# --- Using classmethod ---
print("Before:", Employee.company)
Employee.change_company("InnoTech")
print("After:", Employee.company)

# --- Using staticmethod ---
Employee.greet()

# --- Creating an object and still works ---
emp1 = Employee("Sahana", 50000)
emp1.greet()   # static method can be called from object too
