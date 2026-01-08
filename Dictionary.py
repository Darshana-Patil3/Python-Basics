
#Dictionary Data Type
#Dictionary represents in {key: value} pairs


# Example 1: Simple dictionary
student = {
    "name": "Darshana",
    "course": "MCA",
    "age": 22
}
print(student)
print(type(student))

# Example 2: Accessing values using keys
print(student["name"])
print(student["course"])
print(len(student))

# Example 3: Adding new key-value pair
student["college"] = "GESCOE"
print(student)


# Example 4: Updating value
student["age"] = 23

print(student)

# Example 5: Dictionary with list as value
portfolio = {
    "name": "Darshana",
    "skills": ["HTML", "CSS", "Python", "Bootstrap"]
}

for skill in portfolio["skills"]:
    print(skill)


# Example 6: Using get() method
# Another way to get item
print(student.get("name"))
print(student.get("hobby", "Not Found"))  

#Key() Functions Item() Functions and Values() Functions
print(student.keys())
print(student.values())
print(student.items())


# Deleting element in Dictionary Using pop()
student = {
    "name": "Darshana",
    "Course" : "MCA",
    "age" : 22,
    "sections" : "A"
}
print(student)

student.pop("age")  # we can also use del student["age"] 
print(student)

# Using Clear() Function clears all the elements in Dictionary it becomes empty Dictionary
student.clear()
print(student)


#Dictionary Looping
# Let's first define dictionary in a different way

new = dict({'name': 'Apple', 'year': 1975, 'founder': 'Steve Jobs and Steve Wozniak'})     # dict is special keyword, wrap your dictionary within dict() 

print(new)
print(type(new))

# simple for loop
for item in new:              # this loops over only keys
  print(item)
  print(item, new[item])      # for each key, let's access its value with new[keyname]


# Shorter way to do the same is to use .items() function
for item, val in new.items():
  print(item, val)

# Loop through only keys & values separately

for key in new.keys():
  print(key)
for xyz in new.values():
  print(xyz)



#Nested Dictionary
# A dictionary within a dictionary
employees = {
    "emp1": {
        "name": "Alice",
        "age": 30,
        "department": "HR"
    },
    "emp2": {
        "name": "Bob",
        "age": 25,
        "department": "IT"
    },
   }
print(employees)
print(employees["emp1"]["name"])  # Accessing nested value
print(type(employees['emp2']))
