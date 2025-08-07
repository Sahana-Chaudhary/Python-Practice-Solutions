
'''
f=open("file.txt")
print(f.read())
f.close

This same can be written using with statement liek this:'''

with open("file.txt", "r") as f:
    f.read()
    
# u dont need to explicitly close the file


