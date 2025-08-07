'''
The random-access memory(RAM) is volatile, and all its contents are lost once a program terminates in order to persist the data forever ,we use files

A file is data stored in a storage device. A python program can talk to file by reading content from it and writing content to it

Volatile--Means in which data is not persisted, stores data temporarily
Non volatile---

*** When we run a program,
Firstly it goes into RAM it stays there temporarily
If the person wants to "persist"/save the data it can be read/write by using file
Data can be stored in HDD(Hard disk drive) which is non volatile and stores data permanently
'''

'''
There are 2 Types of files to store data
1. Text file- .txt, .c , .py ...etc
2. Binary files - .jpg, .dat ...etc
and many more

'''

# f = open("File.txt")
# data = f.read()
# print(data)
# f.close()

'''
Built in function:
1. open()- for opening files
It takes 2 parameters--filename and mode

Example--- open("this.txt", "r")
*** by default it is in read mode--r
'''

'''
Reading a file :
f = open("this.txt","r")
text = f.read()
print(text)
f.close()

'''

'''
Functions:
f.read()
f.write()
f.close()

f.readlines()-- to read all lines at once and return them as list of strings
f.readline()-- reads one line at a time from file

'''

#for readlines()

# f=open("file.txt")
# lines=f.readlines()
# print(lines)
# print(type(lines))
# f.close

#for readline()

# f= open("file.txt")
# line1=f.readline()
# line2=f.readline()
# line3=f.readline()
# print(line1, type(line1))
# print(line2, type(line2))
# print(line3, type(line3))
# f.close

#above this is very hectic process so we can just use while loop

line= f.readline()
while(line!=""):    #this is done just because readline runs until list becomes empty
    print(line)
    line=f.readline()
f.close()

'''
modes of opening a file:
r- open for reading
w- open for writing
a- open for appending
+- open for updating
rb- open for read in binary mode
rt- open for read in text mode

'''
