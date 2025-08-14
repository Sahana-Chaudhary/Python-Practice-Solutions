#Write a program to mine a log file and find out whether it contains 'python'

with open("ch9_File_input_output\Practice questions\ch9_06_log.txt","r") as f:
    content=f.read()

if("python" in content):
    print("It is present")
else:
    print("not present")