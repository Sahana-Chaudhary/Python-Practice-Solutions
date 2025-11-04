# Q3. Create a class Rectangle
# Attributes: length, breadth
# Methods:
# area()
# perimeter()
# Create two objects and compare which rectangle has a greater area.

class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
rec1=Rectangle(20,40)
print("Area: ", rec1.area())
print("Perimeter: ", rec1.perimeter())

rec2=Rectangle(30,80)
print("Area: ", rec2.area())
print("Perimeter: ", rec2.perimeter())

print("Greater area: ", "rec1" if rec1.area()> rec2.area() else "r2")