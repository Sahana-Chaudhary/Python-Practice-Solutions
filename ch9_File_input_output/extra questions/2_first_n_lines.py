#Write a Python program to read first n lines of a file.

n=int(input("Enter the number: "))
with open("ch9_File_input_output/extra questions/2_file.txt","r") as f:
    lines=f.readlines()                     #to read all the lines at once
    for line in lines[:n]:
        print(line.strip())
                                        

# lines[:n] is a slice of the first n lines.
# If n is larger than the file’s line count, you just get all available lines—no error.

# Iterates over only those first n strings.
#strip() removes leading and trailing whitespace, including \n, spaces, and tabs.
#Prints the line content “cleanly”


