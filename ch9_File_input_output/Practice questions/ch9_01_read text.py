#WAP to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'

f = open("ch9_01_poems.txt")                             #open the file
content= f.read()                                        #read the file and save in content
if("twinkle" in content):                                #check if it is present in content
    print("The word twinkle is present in the content ")
else:
    print("The word twinkle is not present in the content ")
f.close()                                                 #close the file