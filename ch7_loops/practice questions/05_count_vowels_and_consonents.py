#WAP to count the number of vowels and consonents in a string

n=input("Enter a string: ")
vowels= "aeiouAEIOU"
v_count=0
c_count=0

for i in n:
    if i.isalpha():
        if i in vowels:
            v_count+=1
        else:
            c_count+=1

print("Vowels: ",v_count)
print("Consonents: ",c_count)