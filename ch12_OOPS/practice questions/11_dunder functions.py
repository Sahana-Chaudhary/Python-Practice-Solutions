#dunder functions starts with __ and end with __ example __add__,__init__
#they let u customize how your objects behave with pythons operations

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y)
    
v1=Vector(2,3)
v2=Vector(4,5)
v3=v1+v2   #inside it does v1.__add__(v2)
print(v3.x,v3.y)

