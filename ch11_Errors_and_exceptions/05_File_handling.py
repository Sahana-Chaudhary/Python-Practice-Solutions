#check if file exists

try:
    with open("data.txt",'r') as f:
        content=f.read()
except FileNotFoundError:
    print("File doesnt exist")