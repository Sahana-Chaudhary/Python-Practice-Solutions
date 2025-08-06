'''
print pattern

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
'''
r=int(input("enter rows you want:"))
for i in range(r, 0,-1):        #--for rows    #how many rows to print
    for j in range(i, 0, -1):         #--for columns
        print(j, end=" ")     #end to keep all of them in same line
    print()           #after each row with 5 stars it moves to next

