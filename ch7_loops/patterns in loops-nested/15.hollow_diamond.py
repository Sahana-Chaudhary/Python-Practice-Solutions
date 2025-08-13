'''
print pattern

    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *

'''
r=int(input("Enter a number: "))
for i in range(1,r+1):                       #upper half
    for space in range(r-i):
        print(" ",end=" ")
    for j in range(1,2*i):
        if j==1 or j==(2*i)-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(r-1,0,-1):                       #lower half
    for space in range(r-i):
        print(" ",end=" ")
    for j in range(1,2*i):
        if j==1 or j==(2*i)-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



