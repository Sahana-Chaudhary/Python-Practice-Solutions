class Employee:
    language = "Py"     #class attribute
    salary = 1200000

    def getInfo():
        print(f"The language is {language}")

harry = Employee()         #harry and rohan is object
harry.language = "JS"        #object attribute/ Instance attributes
print(harry.salary, harry.language)

