#what will be the length of following set
s=set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))

#length will be 2 ---20 and 20.0 is considered the same
#means float and int are considered same but not the string
