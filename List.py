#4 Collection Data Types - List, Tuple, Set, Dictionary.

#List Data Type
Flowers = ['Rose','Lotus','Lily','Hibiscus']
print(Flowers)
print(type(Flowers))
print(Flowers[0])
print(Flowers[3])
print(Flowers[0:2])
print(Flowers[2:])
print(Flowers[-1])

#Adding and Removing elements in List
num = [10, 20, 30, 40, 50]
print("Numbers List:", num)
num.append(60)
num.remove(20)
print("New list:", num)

#mixed data type list
mixed_list = [10, 'Hello', 25.5, True]
print("Mixed List:", mixed_list)
print("First Element:", mixed_list[0])



# List Functions
num =[1,2,3,4,5]
print(num)
num.append(6)          # Adding element at the end
print(num)

# To insert an element somewhere in the middle, say 3rd index
Subjects = ['Math', 'Science', 'History']
Subjects.insert(3, 'English')  # Inserting 'English' at index 3  
print(Subjects)

#Using append() insert elements
list = ["Apple", "Banana", "Cherry", "Date"]
list.append("Elderberry")
print(list)
list.pop()
print(list)

#lets define new list
fruits = ['mango', 'apple', 'orange', 'kiwi', 'pineapple', 'papaya']
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)


# to check length of list, use len()
countries = ['Russia', 'India', 'US', 'Japan', 'Germany', 'Italy', 'Zambia']
print(len(countries))

print(len('HELLO'))  # length of string

nums = [8, 4, 2, 1, 16]     
print(max(nums))
print(min(nums))
print(sum(nums))

for item in countries:            # item could be changed by any other random name. 
  print(item)


flowers = [['Rose', 'Lotus'], ['Lily', 'Hibiscus'], ['Sunflower', 'Daisy']]
print(flowers)
print(len(flowers))
print(flowers[0])
print(flowers[1][1])  # Accessing 'Hibiscus' from the nested list




#Creating a list through user input
items = []
n = int(input("Enter number of items to add to the list: "))

for i in range(n):
    item = input("Enter item {}: ".format(i+1))
    items.append(item)
print("Your List:", items)