#A spam comment is defined as the text containing following keywords : "Make a lot of money", "buy now", "subscribe this", "click this".
# Write a program to detect these spams

p1="Make a lot of money"
p2="buy now"
p3= " subscribe this"
p4="click this"

m=input("ENter your comment: ")

if((p1 in m) or (p2 in m) or (p3 in m) or (p4 in m)):   # use 'in' 
    print("spam")
else:
    print("not spam")

