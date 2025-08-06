'''
print pattern

* * * * 
* * *
* *
*
'''
r=int(input("enter rows you want:"))
for i in range(r,0,-1):        #--for rows #for reverse -1
    for j in range(i):         #--for columns
        print("*", end=" ")     #end to keep all of them in same line
    print()           #after each row with 5 stars it moves to next
