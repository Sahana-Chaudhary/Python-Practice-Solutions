# Write a Python program to append text to a file and display the text.

with open("ch9_File_input_output/extra questions/3_file.txt","a") as f:
    f.write("You are amazing")

print("Line appended successfully")

with open("ch9_File_input_output/extra questions/3_file.txt","r") as f:
    content = f.read()
    print(content)