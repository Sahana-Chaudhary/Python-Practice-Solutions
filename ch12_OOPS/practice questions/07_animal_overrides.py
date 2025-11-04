# Q7. Implement Inheritance
# Create classes:
# Animal (method: speak())
# Dog inherits Animal and overrides speak() method

class Animal:
    def speak(self):
        print("Bhow")
    
class Dog(Animal):
    def speak(self):
        print("woof")

a=Animal()
a.speak()

b=Dog()
b.speak()
    
