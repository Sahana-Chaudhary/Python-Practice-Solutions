# python function to print first n lines of this pattern 
'''
***     # for n=3
**
*

pattern = "*" * n
pattern = "*" * n-1
pattern = "*" * n-2
'''

def pattern(n):
    if(n==0):
        return
    print("*" * n)
    return pattern(n-1) 

n=int(input(" Enter n: "))
pattern(n)

