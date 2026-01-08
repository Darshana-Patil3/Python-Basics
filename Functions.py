
#Functions in Python
def greet():
    print("hello, Welcome to Python Functions")
greet()

# Example 2: Function with parameters
def student(name, course):
    print("Student Name:", name)
    print("Course:", course)

student("sakshi", "MCA")
student("radha", "BCA")


# Let's pass some argument to the function

def hello (name):
  print(f'hello {name}')    # Note, the function body is limited by indentation. As long as it is there, it's a part of function body. 

hello('John')
hello(12)
print(type(hello))   

# In Functions add two numbers
def addthis(first, second):
  print("Addition of two numbers is:", first + second)

addthis(45, 55)

#Another method to adding two numbers and return the value
def add_numbers(a, b):
    return a + b
result = add_numbers(10, 20)
print("Sum is:", result)

#OR
def add_numbers(a, b):
    total = a + b
    return total

result = add_numbers(15, 25)
print("Addition Result:", result)


