# Q10. Demonstrate Polymorphism
# Write a common function make_sound(animal) that accepts Dog, Cat, and Cow objects — each having a sound() method.

class Dog():
    def sound(self):
        print("Bark")

class Cat():
    def sound(self):
        print("Meow")

class Cow():
    def sound(self):
        print("Moo")

def make_sound(animal):
    animal.sound()

d = Dog()
c = Cat()
e = Cow()

make_sound(d)
make_sound(c)
make_sound(e)


