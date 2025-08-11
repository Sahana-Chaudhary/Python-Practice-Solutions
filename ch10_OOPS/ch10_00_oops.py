'''
Solving a program by creating object is one of the most popular approaches in programming. This is called oop

It focuses pn reusable code (do not repeat yourself)
'''

# Class- Blueprint of creating an object
# syntax---class Employee:

#Object -Instantiation of class.
#When class is defined, a template(info) is defined. Memory is allocated only after object instantiation

#Example a form---- when its blank its a class, when someone filled it with information- it became an object

#basic class
# class Employee:
#     language = "Py"
#     salary = 1200000

# a = Employee()          #a is object
# print(a.salary, a.language)


'''
Modeling a problem in oops
*Identify the following:
1. Noun- Class -Employee
2. Adjective- Attributes- name, age, salary
3. Verbs- Methods - getSalary(), increment()

'''

#Class Attribute - An attribute that belongs to a class rather than a particular object

class Employee:
    language = "Py"     #class attribute
    salary = 1200000

harry = Employee()         #harry and rohan is object
harry.name = "Harry"        #object attribute/ Instance attributes
print(harry.salary, harry.language, harry.name)

rohan = Employee()              #Every object in this class will get same language and salary
rohan.name = "Rohan"
print(rohan.language, rohan.name)

# HERE name is object attribute/Instance attribute---because made inside object
# language and salary are class attributes because they belong to class
# ****instance attribute take preference over class attributes during assignment and retrieval.


