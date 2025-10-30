#WAP to generate prime numbers between 1-100

for num in range(2,101):
    is_prime=True
    for i in range(2,int(num**0.5)+1):                #we took the square root of that number because then we need to check till square root only and it increases the efficiency of the code
        if num%i==0:
            is_prime=False
            break
    if is_prime:
            print(num,end=" ")
