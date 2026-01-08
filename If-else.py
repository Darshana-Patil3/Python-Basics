
#IF-Else Statements in Python

# Example 1: Simple if 
a = 10
b = 32
if b > a:
  print("b is greater than a")

# Check even and odd numbers
num =int(input("Enter the number:"))

if num % 2 == 0:
   print("It is even number")
if num % 2 != 0:
   print("It is odd number")
if num == 0:
    print("It is zero")


#If-Else Example

# Compare two numbers
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# Voting Eligibility Example
age = 18
if age >= 18:
    print("You are eligible to vote.")
else:
   print("Your not eligible to vote.") 

#If-Elif-Else Example

# Positive, Negative or Zero
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")


# marks example
marks = int(input("Enter your marks:"))
            
if marks > 80 and marks <= 100:
    print("You are in A grade")
elif marks > 60 and marks <= 80:
    print("You are in B grade")
elif marks >= 35 and marks <= 60:
    print("You are in C grade")
else:
   print("Sorry you are fail !!") 

#Nested IF

# You can have if statements inside if statements, this is called nested if statements.

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")