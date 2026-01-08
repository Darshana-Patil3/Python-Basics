
#While loop in python

# Using while loop until condition getting true
# while x is less than 5, keep printing

x = 1
while x < 5:        
    print(x)
    x += 1      # means x = x + 1
# o/p : 1 2 3 4
print('------------')


# When the break statement is encountered, it brings control out of the loop.
# When we want to end the block at certain point, we use break statement.

x = 1
while x < 10:
    if x == 4:
        break
    print(x)
    x += 1
# o/p : 1 2 3   
print('------------')

# To keep running while loop forever, use while True

while True:
    name = input('Input name: ')
    if name == 'stop':
        break
    print("Your name is:", name)
print('------------')

# When you encouter the letter 't', stop. Till then continue.
i = 0  
str1 = 'Beautiful'  
  
while i < len(str1):   
    if str1[i] == 't':   
        i += 1  
        break  
    print('Current Letter :', str1[i])   
    i += 1 