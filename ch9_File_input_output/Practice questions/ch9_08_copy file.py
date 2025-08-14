#write a program to make a copy of a text file "this.txt"

with open("ch9_File_input_output\Practice questions\ch9_08_this.txt") as f:
    content = f.read()

with open("ch9_File_input_output\Practice questions\ch9_08_copy.txt","w") as f:
    f.write(content)