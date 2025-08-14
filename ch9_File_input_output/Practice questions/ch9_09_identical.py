#write a program to find out whetehr a file is identicle or not and matches content of other file or not

with open("ch9_File_input_output\Practice questions\ch9_08_this.txt","r") as f:
    content1=f.read()

with open("ch9_File_input_output\Practice questions\ch9_08_copy.txt","r") as f:
    content2=f.read()

if(content1==content2):
    print("files are identical")
else:
    print("files are not identical")

    