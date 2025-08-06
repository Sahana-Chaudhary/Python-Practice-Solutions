'''
print pattern

1
1 2 
1 2 3
1 2 3 4
1 2 3 4 5
'''
r=int(input("enter rows you want:"))
for i in range(1,r):        #--for rows    #how many rows to print
    for j in range(1,i+1):         #--for columns
        print(j, end=" ")     #end to keep all of them in same line
    print()           #after each row with 5 stars it moves to next

