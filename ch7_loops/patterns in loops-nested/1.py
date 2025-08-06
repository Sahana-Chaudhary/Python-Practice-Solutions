'''
print pattern

* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''

for i in range(1,6):        #--for rows
    for j in range(1,6):         #--for columns
        print("*", end=" ")     #end to keep all of them in same line
    print()           #after each row with 5 stars it moves to next
