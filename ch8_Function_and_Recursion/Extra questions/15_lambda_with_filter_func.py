#use a lambda with the filter() function to get all even numbers from a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_no = list(filter(lambda x : x%2 ==0, numbers))            #lambda function for even no it
print(even_no)                                                 #filter functions filters out even number
                                                            #list used to convert result into list

