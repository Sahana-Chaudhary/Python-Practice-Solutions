#WAP to find out whether a given name is present in list or not
 
list=["sahana","sagarika","rita","sita"]   #case sensitive

name=input("Enter the name: ")

if(name in list):
    print("yes, present in list")
else:
    print("no, not present")

