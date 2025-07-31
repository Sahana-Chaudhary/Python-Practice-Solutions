#WAP to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. 
#assume 3 subjects and take marks from users

M1=int(input("Enter marks of subject 1: "))
M2=int(input("Enter marks of subject 2: "))
M3=int(input("Enter marks of subject 3: "))

total_percentage = 100* ((M1+M2+M3))/300

if(total_percentage>40 and M1>33 and M2>33 and M3>33):
    print("pass",total_percentage)
else:
    print("fail")
