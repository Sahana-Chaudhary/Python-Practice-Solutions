# Q1. Create a class Car
# Attributes: brand, model, year
# Method: display full details of the car
# Practice Tip: Create 2–3 car objects and display their details.

class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    
    def showDetails(self):
        print("Brand: ",self.brand)
        print("Model: ",self.model)
        print("Year: ",self.year)

car1=Car("Toyota","abc",2003)
car1.showDetails()

