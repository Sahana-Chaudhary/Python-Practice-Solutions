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
    for space in range(r-i):
        print("  ",end="")
    for star in range(i):
        print("* ",end="")
    print()