# A file contains a word "Donkey" multiple times. You need to write a program which replace this word
#with ##### by updating the same file

word = "donkey"
with open("Practice questions/ch9_04_donkey.txt", "r") as f:
    content= f.read()

contentNew=content.replace("donkey","#####")

with open("Practice questions/ch9_04_donkey.txt", "w") as f:
    content= f.write(contentNew)

