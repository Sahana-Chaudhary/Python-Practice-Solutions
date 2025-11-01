import os
print(os.getcwd())

print(os.listdir())

os.mkdir("test_folder")

if os.path.exists("test_folder"):
    print("exists")