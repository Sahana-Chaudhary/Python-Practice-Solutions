#Q5. Demonstrate Constructor Overloading using __init__
# Create a class Book with default and parameterized constructors.
# Create objects using both forms.

class Book():
    def __init__(self,title="unknown",author="me"):
        self.title =title
        self.author=author

    def show(self):
        print(f"Book: {self.title} by {self.author}")

book1=Book("ABC","Sahana")
book1.show()
book2=Book()
book2.show()           