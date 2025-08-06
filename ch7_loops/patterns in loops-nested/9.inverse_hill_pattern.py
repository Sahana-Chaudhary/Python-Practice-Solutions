'''
print pattern

* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''
r=int(input("Enter number: "))
for i in range(r,0,-1): 
    for space in range(r-i):    #for space
        print("  ",end="")         #double space for alignment
    for star in range(1,2*i):      #for star
        print("* ",end="") 
    print()                            #for printing the whole patttern in next line