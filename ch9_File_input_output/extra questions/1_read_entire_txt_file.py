#Write a Python program to read an entire text file.

with open("ch9_File_input_output/extra questions/1_file.txt","r") as f:            #to open file in read mode
    content = f.read()                                    #to read the content
    print(content)
    # f.close()                     with with you dont need to do close file

