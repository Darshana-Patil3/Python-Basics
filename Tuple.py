# Tuple Data Type

# In Tuple it can be allow duplicate values

my_tuple = (10, 20, 30, 40, 50, 10, 20)
print(my_tuple)
print(type(my_tuple))
print(len(my_tuple))

# Accessing elements in Tuple
print(my_tuple[0])
print(my_tuple[-1])

# Slicing in Tuple
print(my_tuple[1:4])

#count() function in tuple
print(my_tuple.count(10))  # counts how many times 10 appears in the tuple

#print one by one element using loop
for item in my_tuple:     
  print(item)


 #combine two tuples using +

print(('x','y','z') + ('a','b','c')) 


# To convert list into a tuple

num = [1, 2, 3, 4]
new = tuple(num)

print(num)
print(new)