#wAp to rename a file to "renamed_by_python.txt"    #same as copy content and delete old file

with open("ch9_File_input_output\Practice questions\ch9_11_abc.txt") as f:
    content=f.read()       

with open("ch9_File_input_output\Practice questions\ch9_11_rename_by_python.txt") as f:
    f.write(content)