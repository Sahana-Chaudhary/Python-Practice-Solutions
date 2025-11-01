#Write a Python program to:
# Create a Python dictionary named data with keys: "Name", "Age", and "City".
# Convert it to a JSON string and save it in a file named output.json.
# Open the file again, read the JSON data, and print it in Python dictionary format.

import json 

data={"Name":"Sahana", "Age":21,"City":"chd"}

with open("output.json",'w') as f:
    json.dump(data,f)

with open("output.json",'r') as f:
    content=json.load(f)
    print(content)
