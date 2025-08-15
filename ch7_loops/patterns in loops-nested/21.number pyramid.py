'''
print pattern

        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
'''

r=int(input("Enter the number: "))
for i in range(1,r+1):
    for space in range (r-i):
        print(" ",end=" ")
    for num in range(1,i+1):
        print(num,end=" ")
    for num in range(i-1,0,-1):
        print(num,end=" ")
    print()