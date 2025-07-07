#dictionary is a collection of key value pairs

a={}   #empty dictionary

a={
    "sa":12,
    "ha":34,
    "na":23,
    0:"ch"    
}
print(a,type(a))
print(a["sa"])   #prints none as output if key not found in dictionary

#properties of dictionary
#1.It is unordered
#2. It is mutable
#3.It is indexed
#4.cannot contain duplicate keys

#Dictionary methods
#get                     #prints error as output if key not found in dictionary
print(a.get("sa"))        #difference between get and normal print(a["sa"])  is --if we use square bracket we get output as error if key doesnot exist in dictionary    --and in get method we get output as none

#items()
print(a.items())

#keys()
print(a.keys())

#values()
print(a.values())

#update
a.update({"sa":99 , "re":100})
print(a)

#pop
#pop item

#Sets--collection of non repetitive elements

#Properties of sets
#1.unordered   --can be printed in any order
#2.unindexed
#3.there is no way to change items in set
#4.cannot contain duplicate values 

s={1,5,32,5,5}
print(s)       #like here 5 is repeated so it will only be printed once

a=set()   #empty set  

##set methods/operations

s={1,5,32,5,5,"Harry"}
print(s,type(s))

s.add(23)    #to add elements to s
print(s,type(s))

#length
print(len(s))

#remove
s.remove(1)
print(s)

#pop  --removes random element
s.pop()
print(s)

#clear---clears your whole set and make it empty
#s.clear()

#union and intersection
a={1,2,3}
b={2,3,4}
print(a.union(b))

print(a.intersection(b))

#subset and superset
print({1,2}.issubset(a))
print(a.issuperset({1,2}))










