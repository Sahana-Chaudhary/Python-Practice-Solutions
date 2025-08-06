'''
print pattern

        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''

r=int(input("Enter number: "))
for i in range(1,r+1):                    
    for space in range(1,r-i+1):        #for space
        print("  ",end="")              #double space for alignment
    for star in range(1, 2*i):           #for star
        print("* ",end="")               #end for printing in next line
    print()

