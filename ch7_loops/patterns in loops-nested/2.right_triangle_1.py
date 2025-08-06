'''
print pattern -right triangle

* 
* * 
* * * 
* * * * 
* * * * *
'''
r=int(input("enter rows you want:"))
for i in range(1,r+1):        #--for rows
    for j in range(1,i+1):         #--for columns
        print("*", end=" ")     #end to keep all of them in same line
    print()           #after each row with 5 stars it moves to next
