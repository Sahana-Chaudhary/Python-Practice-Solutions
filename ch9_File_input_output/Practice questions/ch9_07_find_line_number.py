# find line number where python is present in log.txt
# use readline


with open("ch9_File_input_output\Practice questions\ch9_06_log.txt","r") as f:
    lines=f.readlines()                   #reads all lines 

lineno=1
for line in lines:
    if("python" in line):
        print(f"It is present in line no. {lineno}")
        break            #goes out of loop if python is present so that else should not work
    lineno +=1

else:                        #for with else---works when for loop gets exhausted
        print("not present")
