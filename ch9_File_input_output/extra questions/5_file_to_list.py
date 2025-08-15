#Write a Python program to read a file line by line and store it into a list.
 
lines_list=[]                                      #created an empty list to store file content 
with open("ch9_File_input_output/extra questions/5_file.txt","r") as f:
    line = f.readline()
    while line:
        lines_list.append(line.strip())               #append() requires an argument — the value you want to add to the list.
        line=f.readline()

print(lines_list)