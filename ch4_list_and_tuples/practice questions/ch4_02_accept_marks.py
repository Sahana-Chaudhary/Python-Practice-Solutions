#WAP to accept marks of 6 students and display them in  a sorted manner

list=[]
a=int(input("Enter the marks: "))
list.append(a)

b=int(input("Enter the marks: "))
list.append(b)

c=int(input("Enter the marks: "))
list.append(c)

d=int(input("Enter the marks: "))
list.append(d)

e=int(input("Enter the marks: "))
list.append(e)

f=int(input("Enter the marks: "))
list.append(f)



list.sort()
print(list)