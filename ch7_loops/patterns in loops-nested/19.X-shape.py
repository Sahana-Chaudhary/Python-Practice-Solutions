'''
print pattern
*     *
 *   *
  * *
   *
  * *
 *   *
*     *
'''

r=int(input("Enter the number: "))    #r should be odd number to make perfect symmetry
for i in range(1,r+1):
    for j in range(1,r+1):
        if j==i or j==r-i+1:
            print("* ",end="")
        else:
            print("  ",end="")
    print()

