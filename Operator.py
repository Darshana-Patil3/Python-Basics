# Arithmatic Operators + - * / % // **
a = 10
b =20
print(a + b)
print(a - b)
print(a * b)
print(b / a)   # division
print(b // a)  # floor division
print(b % a)   # modulus
print(a ** 2)  # exponentiation
print(type(b / a))

# Python supports BODMAS rule when multiple operators are in line
print(6 * 3 + 1)          # first multilpication will be executed
print(2 + 5 * 4)          # same as above first multilpication will be executed
print(5 * (4 + 1) )       # first brackets then rest 

#Comparison Operators  > < >= <= == !=
a = 40
b = 50
print(a > b)   #False
print(a < b)   #True
print(a >= b)  #False
print(b <= a)  #False
print(a == b)  #False
print(a != b)  #True

# == checks whether left hand side and right hand side is equal

print(2 == 2)   # if LHS = RHS, output True else False
print(2 == 1)   # Here LHS is not equal to RHS

# Let's explore < > <= >=

print(3 != 2)
 
print(3 > 2)
print(5 < 2)
 
print(3 >= 3)
print(3 >= 2)
 
#Assignment Operators =  +=  -=  *=  /=  //=  %=  **=
x = 5
print(x)
x += 3     # x = x + 3
print(x)

x -= 2      # x = x - 2
print(x)

x *= 4      # x = x * 4
print(x)

x /= 2     # x = x / 2
print(x)

#logical Operators and, or, not
 
a= True
b = False

print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)


#abs() function gives positive numbers
num1 = -5
print(abs(num1))
num2 = -3.2
print(abs(num2))

#round() function rounds the float number to nearest integer
p = 3.6
q = 2.3

print(round(p))
print(round(q))


#Type Casting
x = '5'
y = '3'
print(x, type(x))
print(y, type(y))
print('Addition =', x + y)

