#loops--to repeat the set of statements
#while loop--condition is checked first . If it is true the body of the loop is executed otherwise 

i=1 
while(i<6):
    print(i)
    i+=1      # increase by 1 then goes back to loop

#WAP to print 1 to 50 using while loop
i=0
while(i<51):
    print(i)
    i+=1

#WAP to print the content of a list using while loops
list=[1, "sa",False , "this", "is", "ha", "na"]
i=0
while(i<len(list)):
    print(list[i])     #to print elements of list
    i+=1

#for loop---used to iterate through a sequence like list,tuple,or string
#range() function --used to generate sequence of number     range(start,stop,step)
for i in range(4):   #will print till 4
    print(i)

for i in range(0,2):
    print(i)

for i in range(0,10,2):
    print(i)

#print elements of list
l= [1,4,6,234,6, 764]
for i in l:
    print(i)

s="sahana"
for i in s:
    print(i)

#for loop with else
#an optional else can be used with a for loop if the code is to be executed when the loop exhausts
#this statement exists when loop gets over

list=[1,2,3,4]
for i in list:
    print(i)
else:
    print("Done")

#Break statement
#used to come out of the loop

for i in range(0,80):
    if i==10:
        break
    print(i)  

#Continue statement
#skip the current iteration of loop and continue with next one 

for i in range(0,80):
    if i==10:     #10 is skipped
        continue
    print(i)

for i in range(4):
    print("printing")
    if(i==2):
        continue
    print(i)

#pass statement
#do nothing
list=[1,2,3]
for i in list:
    pass












