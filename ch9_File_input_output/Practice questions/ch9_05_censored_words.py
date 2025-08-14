#wap for list of words to be censored

words = ["donkey","bad","worse"]
with open("ch9_File_input_output/Practice questions/ch9_04_donkey.txt", "r") as f:
    content= f.read()

for word in words:
    content=content.replace(word,"#" * len(word))

with open("ch9_File_input_output/Practice questions/ch9_04_donkey.txt", "w") as f:
    content= f.write(content)