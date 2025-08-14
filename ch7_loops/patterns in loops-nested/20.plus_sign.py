'''
print pattern

     *   
     *
     *
* * * * * * *
     *
     *
     *
'''
r=int(input("Enter the number: "))            #should be odd for perfect symmetry
mid=r//2+1

for i in range(1,r+1):
    for j in range(1,r+1):
        if j==mid or i==mid:
            print("* ",end="")
        else:
            print("  ",end="")
    print()
    