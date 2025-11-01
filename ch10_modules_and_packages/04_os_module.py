#Print the current working directory
# List all files and folders in that directory
# Create a new folder named "test_folder"
# Check if the folder exists using os.path.exists()

import os
print(os.getcwd())

print(os.listdir())

os.mkdir("test_folder")

if os.path.exists("test_folder"):
    print("exists")

    