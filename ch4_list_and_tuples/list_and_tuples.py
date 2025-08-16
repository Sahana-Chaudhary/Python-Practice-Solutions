#python lists are containers to store a set of values of any datatype'
#strings are immutable- cannot change
#list are mutable

a=["Apple","Orange", 5, 345.06]
print(a[0])
print(a)

a[1]=2
print(a)
print(a[0:2])

# list functions
#append() function
a.append("abc")
print(a)

#sort(),reverse(),insert(4,3),pop(1),remove(1) function
l1=[1,4,5,2]
l1.sort()
l1.reverse()
print(l1)

l1.insert(3,333)    #(index,object)
print(l1)

l1.pop(3)   #(index)
print(l1)
value=l1.pop(3)
print(value)
print(l1)

l1.remove(5)    #element not index
print(l1)

#tuple
#collection of data types--immutable

a=(1,2,3,4)
print(a)
print(type(a))

#empty tuple
b=()
print(b)

#tuple for single element
c=(1,)
print(type(c))

#a[0]=10        #cant do because tuple is immutable
#print(a)

#tuple methods

#count   
d=(1,45,342,45,3424,False,"Rohan","Shivam")
no=d.count(45)
print(no)

#index   ---returns index that comes first
i=d.index(45)
print(i)

#to repeat 
g=d*3
print(g)

#in---to check if element exists in tuple
print(2 in d)
print(45 in d)

#len---to check length of tuple
print(len(d))

#min and max--- to find minimum and maximum element in tuple
h=(75,9789,45,33)
print(min(h))
print(max(h))

#slicing
i=h[1:4]
print(i)

#unpacking   --can unpack into individual variables
j,k,l,m =h
print(j,k,l,m) 

