#write program to calculate grade of student from marks

m=int(input("Enter your marks: "))

if(m>=90 and m<=100):
    grade="Ex"
elif(m>=80 and m<90):
    grade="A"
elif(m>=70 and m<80):
    grade="B"
elif(m>=60 and m<70):
    grade="C"
elif(m>=50 and m<60):
    grade="D"
else:
    grade="F"

print("your grade is: ", grade)


