#Create an empty dictionary . Allow 4 frineds to add their favourite language as value and use key as their names . Assume the names are unique

d={}
name=input("Enter your name: ")
lang=input("Enter language name: ")
d.update({name:lang})     #used update function so that it comes in order

name=input("Enter your name: ")
lang=input("Enter language name: ")
d.update({name:lang})

name=input("Enter your name: ")
lang=input("Enter language name: ")
d.update({name:lang})

name=input("Enter your name: ")
lang=input("Enter language name: ")
d.update({name:lang})

print(d)

#ques 7 --if names of 2 friends are same then what will happen?
# It will update and take the last value for the name not the first

#ques 8:if language of 2 friends are same then what will happen?
# It will be same because values can be same, keys should not be same

