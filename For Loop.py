
#FOR LOOP IN PYTHON

# Use for loop to iterate through a list
Dishes = ['Pizza', 'Burger', 'Pasta', 'Salad']

for Dishes in Dishes:
    print(Dishes)

# Use for loop to iterate through a tuple
Countries =('India', 'USA', 'Germany', 'France')

for Countries in Countries:
    print(Countries)

# Use for loop to iterate through a dictionary
student = {
    "name": "Darshana",
    "Course" : "MCA",
    "age" : 22,
    "sections" : "A"
}

for sentense in student:
    print(sentense,student[sentense])

# Use for loop to iterate through a string
message = "hey, nice to meet you."
for i in message:
    print(i)

# range() 

for i in range(5):
    print(i)

print('------------')

for i in range(4,11):
    print(i)


# Use enumerator for getting index
courses = ['ba', 'bcom', 'bsc', 'be']

for id, item in enumerate(courses):
  print(id, item)

#use condition inside for loop
Dishes = ['Pizza', 'Burger', 'Pasta', 'Salad', 'Fries']

for Dishes in Dishes:
    if Dishes == 'Fries':
        print("I love Fries")
    else:
        print('Dishes is not Fries')


#print text one by one using loop
name = input('enter your name --- ')
for char in name:
  print(char)

#write a function that calculate square of each number
numbers = [1, 2, 3, 4, 5]

def sqr(item):
  return item * item

for i in numbers:
  print(i, sqr(i))


# Total number of given list

num = [1, 2, 3, 4, 5]
total = 0
for i in num:
   total = total + i
   print("Total is", total)


# This gives multiplication table of number n given by user input

num = int(input("Enter the number "))  
for i in range(1,11):  
    c = num * i  
    print(num, 'x', i, '=', c)

print('--------------------------')
# print pyramid pattern using for loop

rows = 5
for i in range (rows):
    for j in range(i + 1):
        print("*", end=" ")
    print(" ")

print('--------------------------')

# print reverse pyramid pattern using for loop

n = 7
for i in range(6,0,-1):
   for j in range(i):
      print("*", end=" ")
   print(" ")