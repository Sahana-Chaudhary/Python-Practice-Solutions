letter = '''Dear <|Name|>,
You are selected
<|Date|>'''

print(letter.replace("<|Name|>","Sahana").replace("<|Date|>","april"))    #chaining of replace function otherwise 
