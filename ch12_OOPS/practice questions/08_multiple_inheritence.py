# Q8. Demonstrate Multiple Inheritance
# Create:
# Parent1 with method show1()
# Parent2 with method show2()
# Child inherits both and uses methods from both parents.

class Parent1():
    def show1(self):
        print("Parent1")

class Parent2():
    def show2(self):
        print("Parent2")

class Child(Parent1,Parent2):
    def show3(self):
        print("Both")

c1=Child()
c1.show1()
c1.show2()
c1.show3()
