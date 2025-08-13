'''
print pattern 
* * * * *
 * * * *
  * * *
   * *
    *
   * *
  * * *
 * * * *
* * * * *
'''


r=int(input("Enter the number: "))    #upper half
for i in range(r,0,-1):
    for space in range(r-i):
        print(" ",end="")
    for star in range(i):
        print("* ",end="")
    print()

for i in range(2,r+1):          #lower half
    for space in range(r-i):
        print(" ",end="")
    for star in range(i):
        print("* ",end="")
    print()
