# Write a Python program that:
# Prints your Python version
# Prints the path of your current script
# Prints the list of all directories where Python looks for modules

import sys

print("Version:",sys.version)
print(sys.argv[0])
print(sys.path)