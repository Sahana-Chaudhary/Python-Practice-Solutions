#Write a Python program to read last n lines of a file.

n=int(input("Enter the number: "))
with open("ch9_File_input_output/extra questions/4_file.txt","r") as f:
    lines=f.readlines()                     #to read all the lines at once
    for line in lines[-n:]:
        print(line.strip())