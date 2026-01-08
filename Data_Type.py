
print("Hello, Welcome To My First Program")

# Data Types and Variables

name ="Python is really fun language"
print(name)
print(type(name))

# Integer and Float Data Types
weight = 40
another_weight = 50.5
print(weight)
print(type(weight))
print(another_weight)
print(type(another_weight))

# Boolean Data Type
is_student = True
print(is_student)
print(type(is_student))



#String basics

msg = "Priya's favorite subject is Math"
print (msg)

msg = 'Priya\'s favorite subject is Math'
print(msg)
print(len(msg))


#string indexing and slicing
my_string = "Hello, World!"
print(my_string[0])  # H
print(my_string[7])  # W
print(my_string[-1]) # !
print(my_string[0:5]) # Hello
print(my_string[2:])  # World!
print(my_string[:5])  # Hello

# String Functions
text = "  Hello, Python Programming!  "
print(text.lower())
print(text.upper())
print(text.title())
print(text.count('m'))
print(text.count('ll'))
print(text.find('p'))
print(text.find('w'))
print(text.find('python'))
print(text.replace('Python', 'Java'))

#Defining another variable
new_text = text.replace('Python', 'Java')
print(new_text)
print(text)

fav_k_actor = "Cha Eun woo"
print(fav_k_actor.replace("Cha Eun woo", "Lee Min Ho"))
print(fav_k_actor.replace("Eun", "Min"))
print(fav_k_actor.replace("Gong","Lee")) # No change because 'Gong' does not exist in the original string

list = "  hey! nice to meet you.   "
print(list)
print(list.strip()) # strip Function

print(len(list))
print(len(list.strip()))

#spliting function
sentence = 'Python is a popular programming language'
print (sentence.split(' '))  # Splitting by space

output = sentence.split(' ')
print(type(output))
print(output)

# Connecting two strings together
first = 'Know'
last = 'ledge'
name = first + last
print(name)

name = first + ' ' + last
print(name)

name = first + '    ' + last
print(name)


# Another way to do the same
name = '{}{}'.format(first, last)
print(name)

name = '{} {}'.format(first, last)
print(name)

name = '  {}     {}  '.format(first, last)
print(name)

name = '  {}     {}  '.format(last, first)
print(name)        
# {} is a special placeholder, that can be used within string,
# and passing the desired variable with .format()

# use the string functions within fstrings
name = f'{first.upper()} {last.lower()}'
print(name)



#Integer & Float Data Types
a = 10
b = 3.5
print(a,b)
print(type(a),type(b))

c= a+b
print(c)

#  using arithmatic operations such as + - * / // %

print(a-b)
print(a*b)
print(b / a)   # division sometimes may result in float
print(b // a)  # this is called floor division i.e. the output is quotient without reminder
print(b % a)   # this is called modulus i.e. the reminder after division
print(a ** 2)  # exponentiation i.e. a raised to the power 2
print(type(b/a))

new1 = 2.1
new2 = 0.3

print(new1 + new2)
print(new1 - new2)


#now input from user
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
print(num1)
print(num2)
print(num1 + num2)  # this will concatenate the two inputs as strings
print(type(num1))
print(type(num2))

text = input('Enter any text-:')    
print(text.upper())
print(text.title())
print(text.find('e'))
print(text.count('e'))
print(text.replace('e','z'))
print(len(text))