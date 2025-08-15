#Use a lambda with the sorted() function to sort a list of tuples based on the second element

data = [('apple', 5), ('banana', 2), ('cherry', 8), ('date', 1)]
sort_by_second =sorted(data,key=lambda x : x[1])                      #tells sorted() to use the number (second item in tuple) for sorting.  [1] means index of item
print(sort_by_second)