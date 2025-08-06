'''
print pattern

    *
   * *
  * * *
 * * * *
* * * * *
'''
r=int(input("Enter number: "))
for i in range(1,r+1):
    for space in range(1,r-i+1):
        print(" ",end="")
    for star in range(i):
        print("* ",end="")
    print()