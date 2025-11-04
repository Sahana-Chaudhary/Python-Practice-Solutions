# Q2. Write a class Student
# Attributes: name, roll number, marks
# Methods:
# display(): prints student info
# is_passed(): returns True if marks > 40 else False

class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks

    def display(self):
        print("Name: ",self.name)
        print("roll_no: ",self.roll_no)
        print("marks: ",self.marks)

    def is_passed(self):
        if self.marks>40:
            return True
        else:
            return False
        
Stu1=Student("Sahana",1,20)
Stu1.display()
print("Passed:",Stu1.is_passed())

Stu2=Student("sana",2,60)
Stu2.display()
print("Passed:",Stu2.is_passed())

