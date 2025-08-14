'''
print pattern 
*             *
* *         * *
* * *     * * *
* * * * * * * *
* * *     * * *
* *         * *
*             *

'''

r=int(input("Enter the number: "))    #upper half
for i in range(1,r+1):
    for star in range(i):
        print("* ",end="")
    for space in range(2*(r-i)):
        print("  ",end="")
    for star in range(i):
        print("* ",end="")
    print()

for i in range(r-1,0,-1):          #lower half
    for star in range(i):
        print("* ",end="")
    for space in range(2*(r-i)):
        print("  ",end="")
    for star in range(i):
        print("* ",end="")
    print()
