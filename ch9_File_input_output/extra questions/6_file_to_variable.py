#Write a Python program to read a file line by line store it into a variable.

with open("ch9_File_input_output/extra questions/5_file.txt","r") as f:            #to open file in read mode
    content = f.readlines()                                    #to read the content

print(content)
