
# class and object in python

#  Simple class with attributes
class laptop:
    Brand = "Lenovo"
    price = 299

lap1 = laptop()
print(lap1.Brand)
print(lap1.price)


# Class with a method
class Car:
    brand = "BMW"

    def show_brand(self):
        print("Car Brand:", self.brand)

m1 = Car()
m1.show_brand()


# The above code is correct, but we'd like to pass name and age when we create object. 
# So this is how we'll modify the code
# Constructor (__init__)
class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def details(self):
        print("Teacher Name:", self.name)
        print("Subject:", self.subject)

t1 = Teacher("sakshi", "Mathematics")
t2 = Teacher("sapna", "English")

t1.details()
t2.details()


# Updating object data
class Account:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def show_balance(self):
        print("Account Holder:", self.holder)
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount

acc = Account("aarush jadhav", 5000)
acc.show_balance()
acc.deposit(2000)
acc.show_balance()


# Using return value
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

c1 = Circle(7)
print("Circle Area:", c1.area())


#  Another real-life example

class Dog:
  def __init__(self, breed, age, color):
    self.breed = breed
    self.age = age
    self.color = color
  def details(self):
    print(f"Breed - {self.breed}, Age - {self.age}, Color - {self.color} ")

dog1 = Dog('Bob', 5, 'Black')

dog1.details()