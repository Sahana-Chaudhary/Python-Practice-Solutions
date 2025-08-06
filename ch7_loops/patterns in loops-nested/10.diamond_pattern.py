'''
print pattern

        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''
r=int(input("Enter number: "))
for i in range(1,r):         #just changes this to r just because lines were repeating
    for space in range(1,r-i+1):          #for space
        print("  ",end="")                # double space to match the alignment
    for star in range(1, 2*i):            #for star
        print("* ",end="")             
    print()                               #for printing the whole patttern in next line

for i in range(r,0,-1):
    for space in range(r-i):
        print("  ",end="")
    for star in range(1,2*i):
        print("* ",end="")
    print()