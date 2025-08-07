#write a python function to remove a given function from the list and strip it at the same time
'''
strip function----remove that thing from word
'''

def rem(l,word):              #l=list of string , word= word to be removed from list
    n=[]                      #n= empty list to store modified data
    for item in l:            #item-- variable name-----just like for i in range
        if not(item==word):   #only process items that is not an
            n.append(item.strip(word))    # removes any characters found in word from the start and end of item, not just the word itself.
    return n                             

l=["sahana", "Rohan", "an", "Risha"]
print(rem(l,"an"))

