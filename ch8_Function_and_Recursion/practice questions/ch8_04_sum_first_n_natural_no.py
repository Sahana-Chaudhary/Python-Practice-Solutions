#recursive function of first n natural numbers
'''
sum of first n natural numbers= n+ n-1 + n-2+  ...3 +2+1
sum = n + sum(n-1)
          sum(n-1)= n-1 + sum(n-2)
                          sum(n-2)= n-2 + sum(n-3)
'''
def sum(n):
    if (n == 0):     #base condition
        return 0    
    return n + sum(n-1)

n=int(input("Enter the number upto which u want sum: "))
print(sum(n))
