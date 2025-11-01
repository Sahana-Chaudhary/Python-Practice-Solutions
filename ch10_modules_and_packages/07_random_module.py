# Write a Python script that:
# Generates a random integer between 1 and 100
# Creates a list of fruits and prints a random fruit from it
# Shuffles the list randomly and prints it

import random as r

print(r.randint(1,100))

l=["apple","banana","guava"]
print(r.choice(l))

r.shuffle(l)
print(l)


