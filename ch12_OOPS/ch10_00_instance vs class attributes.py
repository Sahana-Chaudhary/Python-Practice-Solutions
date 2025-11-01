class Employee:
    language = "Py"     #class attribute
    salary = 1200000

harry = Employee()         #harry and rohan is object
harry.language = "JS"        #object attribute/ Instance attributes
print(harry.salary, harry.language)

#here when we have language in both attributes that is class and object ------object/instance attribute will be taken into consideration

