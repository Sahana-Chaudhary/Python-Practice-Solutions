#Snake, water, Gun game
'''
1 for snake
-1 for water
0 for gun
'''

import random               #to generate a random choice for the computer.

computer = random.choice([-1,0,1])  #computer choice


you_choice= input("Enter your choice(s/w/g): ")           #your choice from s/w/g 

youDict = {"s":1, "w":-1 , "g":0 }      #use dictionary for assigning value
reverseDict = {1: "Snake", -1:"Water", 0: "Gun"}       #to convert input value back to string

you = youDict[you_choice]                         #convert user input to numeric

print(f"Computer chose {reverseDict[computer]}")              #show the choices in output by using reverse mapping
print(f"You chose {reverseDict[you]}")

if(computer==you):
    print("Draw!")             

else:
    if(computer==-1 and you==1):
        print("You win!")
    elif(computer==1 and you==0):
        print("You win!")
    elif(computer==0 and you==-1):
        print("you win!")

    elif(computer==1 and you==-1):
        print("You lose!")
    elif(computer==0 and you==1):
        print("You lose!")
    elif(computer==-1 and you==0):
        print("You lose!")
    else:
        print("Something went wrong!!!!")




