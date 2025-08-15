#Create a function with keyword arguments
#Create a function print_info(**kwargs) that accepts keyword arguments and prints the key-value pairs. 
#Call it with different keyword arguments

def func1(**kwargs):
    if kwargs:
        print("\n--Info----")
        for key,value in kwargs.items():
            print(f"{key}:{value}")
    else:
        print("\n no info")
    
func1(name="Alice", age=30,city="new york")
func1(name="abc",salary=5678899)
func1()   #no arguments

        