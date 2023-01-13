# Defining variables

x = 15 
price = 9.99
discount = 0.2
result = price * (1 - discount)
print(result) 

# String formatting

name = "Bob"
greeting = "Hello, {}"
with_name = greeting.format(name)
print(with_name)

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Rolf", "Monday")
print(formatted)

# Getting user input

name = input("Enter your name: ")
print(name)

size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)
square_meters = square_feet / 10.8 #convert string to number
print (f"{square_feet} square feet is {square_meters:.2f} square meters.") # f string, limits to 2 float points

# Writing an app

user_age = input("Enter your age: ")
years = int(user_age)
months = years * 12
print(f"Your age, {years}, is equal to {months} months.")

# OR

user_age = int(input("Enter your age: "))
months = user_age * 12
print(f"Your age, {user_age} is equal to {months} months.")

# Lists, tuples, and sets

l = ["Bob", "Rolf", "Anne"] # Can add or remove elements from list, keeps order
t = ("Bob", "Rolf", "Anne") # Cannot add or remove elements from tuple, keeps order
s = {"Bob", "Rolf", "Anne"} # Cannot have duplicate elements, can add or remove elements, order can change
print(l[0]) # [] can be used on lists and tuples, subscript notation does not work on sets
l[0] = "Smith" # This cannot work on tuples, tuples cannot be modified, cannot use on sets
print(l) # first element printed is Smith, then Rolf, then Anne
l.append("Smith") # list will now have Smith tacked to the end, cannot work on tuples
l.remove("Rolf") # removes Rolf
print(l) # Can see that Rolf is removed
s.add("Smith")
print(s) # Works, but the order can be different
s.add("Smith") # Ignored, Smith is already added

# Advanced set operations

friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}
local_friends = friends.difference(abroad) # finds difference between two sets
print(local_friends) # prints Rolf
local_friends = abroad.difference(friends)
print(local_friends) # empty set printed
local = {"Rolf"}
friending = local.union(abroad) # pritns Anne, Bob, and Rolf
print(friending)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}
both = art.intersection(science)
print(both)

# Booleans

print(5 == 5) # == used to compare two elements exactly (true)
print( 5 > 5) # false
print(10 != 10) # false
# Comparisons: ==. !=. >, <, >=, <= and can use these on different data types
friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]
print(friends == abroad) # true
print(friends is abroad) # false, when creating a new list, it has its own area in memory, and is not the same "thing"
# abroad = friends instead will return true

# If statements

day_of_week = input("What day of the week is it today? ").lower() # makes input lowercase
print(day_of_week == "monday") # replaced by true or false
if day_of_week == "monday": 
    print("Have a great start ot your week!") # indentation is important
elif (day_of_week == "tuesday"):
    print("It's Tuesday.")
else:
    print("Full speed ahead!")
print("This always runs.")

# In keyword

friends = ["Rolf", "Bob", "Jen"]
print("Jen" in friends)

movies_watched = {"The Matrix", "Green Book", "Her"} # using a set because movies are unique, we don't care about the order either
user_movie = input("Enter something you've watched recently: ")
print(user_movie in movies_watched)

# If statements with in keyword

#uses above code
if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print("I haven't watched that yet.")

number = 7
user_input = input("Enter 'y' if you would like to play: ").lower()
if user_input == "y":
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif number - user_number in (1, -1): # or elif abs(number - user_number) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")

# Loops

number = 7
while True: # will need to terminate loop within loop's code
    user_input = input("Would you like to play? (Y/n) ")
    if user_input == "n":
        break
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif number - user_number in (1, -1): # or elif abs(number - user_number) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")

friends = ["Rolf", "Jen", "Bob", "Anne"]
for friend in friends:
    print(f"{friend} is my friend")
for friend in range(4): # repeats 4 times, creates a list of numbers
    print(f"{friend} is my friend.")

grades = [35, 57, 87, 100, 100]
total = 0
amount = len(grades)

for grade in grades: 
    total += grade
print(total/amount) # gives average

# OR

total = sum(grades)
print(total/amount)

# List comprehension

numbers = [1, 2, 3]
doubled = [num * 2 for num in numbers]

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]
print(starts_s)

# Dictionaries

friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
print(friend_ages["Adam"])
friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27}
]
print(friends[1]["name"])

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
for student, attendance in student_attendance.items():
    print (f"{student}: {attendance}%")
if "Bob" in student_attendance:  # Bob below has to be in single quotes
    print(f"Bob: {student_attendance['Bob']}%") 
else: 
    print("Bob is not a student in this class.")
attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))

# Destructuring variables

# x = (5, 11) brackets are actually not necessary for tuples unless you are explicit
t = 5, 11
x, y = t
print(x, y) # python will split that tuple so that x is 5 and y is 11

print(list(student_attendance.items())) # returns list of tuples
# for student, attendance in student_attendance.items(): will deconstruct to two components like before

people = [("Bob", 24, "Mechanic"), ("James", 24, "Aritst"), ("Harry", 32, "Lecturer")]
for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}") # unpacking will need the same number of variables
for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")
# the _ variable name is only for variables meant to be ignored

head, *tail = [1, 2, 3, 4, 5] # asterisk is meant for a name to collect
print(head) # prints 1
print(tail) # prints 2, 3, 4, 5 in a list
# *head would be 1, 2, 3, 4 not in a list and tail alone would be 5

# Functions

def hello():
    print("Hello!")
hello() # calls function hello
def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}.")
user_age_in_seconds()

# Function arguments and parameters

def add(x, y):
    result = x + y
    print(result)
    pass # pass means to do nothing
add(5, 3)

def say_hello(name, surname):
    print(f"Hello, {name} {surname}.")
say_hello("Bob", "Smith") # Bob enters function as the argument "name", Smith enters as "surname"
say_hello(surname="Bob", name="Smith") # named/keyword arguments will return Smith Bob instead

def divide(dividend, divisor):
    if divisor !=0:
        print(dividend/divisor)
    else:
        print("You fool!")
divide(dividend=15, divisor=0) # typically don't add spaces for arguments, positional arguments have to go first

# Default paramter values

def add(x, y=8): # means x is necessary to run, y is not and will default to 8. default parameters MUST be at the end
    print(x + y)
add(5, 8)
add(5) # runs same result (13)

default_y = 3
def add(x, y=default_y): # y will be created and will not change even if you change default_y later
    sum = x + y
    print(sum)
add(2)
default_y = 4 # changing a variable only changes it globally
add(2) # will still be 5

# Functions returning values

def add(x, y):
    print(x + y)
add(5, 8)
result = add(5, 8)
print(result) # functions return None by default, result = None here
def add(x, y):
    return x + y # code after this will never get called because returns exit functions
result = add(5, 8)
print(result) # Now prints 13

# Lambda functions

lambda x, y: x + y # returns outputs, has no name but can assign it to a variable name, is short
# to use lambda function:
print((lambda x, y: x + y)(5, 7)) # not common to do this

def double(x):
    return x * 2
sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence] # doubles the sequence, usually better than the below
doubled = map(double, sequence) # exactly the same as the above list comprehension
doubled = [(lambda x: x * 2)(x) for x in sequence] # the first example with lambda
doubled = list(map(lambda x: x * 2, sequence)) # the second example with lambda, a bit better than before

# Dictionary comprehensions

users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob234"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234")
]
username_mapping = {user[1]: user for user in users}
print(username_mapping) # prints entire tuple
print(username_mapping["Bob"])
username_input = input("Enter your username: ")
password_input = input("Enter your password: ")
_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your details are correct!")
else:
    print("Your details are incorrect.")

# Unpacking function arguments

def multiply(*args): # collecting arguments
    print(args)
    total = 1
    for arg in args:
        total = total * arg # if a tuple is passed, it will be 1 * the tuple to just be the tuple as a data point
    return total
multiply(1, 3, 5) # puts in 3 arguments but is collected into one args argument, returns 15

def add(x, y):
    return x + y
nums = [3, 5]
add(*nums) # uses 3 for x and 5 for y, without the * will put the list into x
nums = {"x": 15, "y": 25}
print(add(**nums)) # tells python to match the dictionary key with the parameter name like x to x as named args

def apply(*args, operator): # says to collect all positional arguments in tuple args and pass in a named argument (operator) at the end
    if operator == "*":
        return multiply(*args) # args passes in a tuple, *args passes in the different arguments to be collected in the multiply function
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."
print(apply(1, 3, 6, 7, operator="+")) # returns 17
print(apply(1, 3, 6, 7, operator="*")) # prints the arguments in a tuple from the previous multiply function and then returns 126

# Unpacking keyword arguments

def named(**kwargs):
    print(kwargs)
details = {"name": "Bob", "age": 25}
named(**details) # unpacks dictionary into keyword arguments

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")
print_nicely(name="Bob", age=25)

def both(*args, **kwargs): # accepts an unlimited # of arguments, typically for all of them to be passed into another argument
    print(args)
    print(kwargs)
both(1, 3, 5, name="Bob", age=25) # prints tuple of args and then a dictionary of args

def myFunction(**kwargs):
    print(kwargs)
# myFunction(**"Bob") # Error, not a dictionary, must be mapping
# myFunction(**None) # Same error!

# Object oriented programming

student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}
def average(sequence):
    return sum(sequence) / len(sequence)
print(average(student["grades"]))

class Student:
    def __init__(self, name, grades): # functions inside of classes are called methods
        self.name = name
        self.grades = grades
    def average_grade(self):
        return sum(self.grades) / len(self.grades)
student = Student("Bob", (90, 90, 93, 78, 90)) # initializes a student from the class Student, Bob becomes the name and the tuple becomes the grades
print(student.name) # prints name
print(student.grades) # prints the tuple of grades
print(student.average_grade()) # prints average, 88.2

# Magic methods

class Person:
    def __init__(self, name, age): # __ indicate magic methods
        self.name = name
        self.age = age
    def __str__(self): # turns object into string
        return f"Person {self.name}, {self.age} years old." # generally print out some nice and easy-to-read string for the user
    def __repr__(self): # used in python debugger, another magic method
        return f"<Person({self.name}, {self.age})>"
bob = Person("Bob", 35)
print(bob) # prints string by using the str method by default
print(bob.__repr__()) # magic methods can still be called this way

# Class methods and static methods

class ClassTest:
    def instance_method(self): # instance methods use the object as the first parameter, used for most things, produces an action using data from the object, can also modify data inside self
        print(f"Called instance_method of {self}")
    @classmethod
    def class_method(cls): # cls with be the class itself, used as factories
        print(f"Called class_method of {cls}")
    @staticmethod
    def static_method(): # does not have parameter cls or self, does not receive anything when called, just used to place a method inside a class
        print("Called static_method.")
ClassTest.class_method() # will auto pass ClassTest in there
ClassTest.static_method() # just a separate function living in the class being called

class Book:
    TYPES = ("hardcover", "paperback")
    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"
    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)
    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, Book.TYPES[1], page_weight)
book = Book("Harry Potter", "hardcover", 1500)
print(book.name)
print(book)
hbook = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)
print(hbook)
print(light)

# Class inheritance

class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True
    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})" # self.name!r defaults to repr method format
    def disconnected(self):
        self.connected = False
        print("Disconnected.")
printer = Device("Printer", "USB")
print(printer)
printer.disconnected()

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity
    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"
    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected.")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages
printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)
printer.disconnected()
printer.print(30) # will show that the printer is not connected, will not execute

# Class composition

class BookShelf:
    def __init__(self, *books):
        self.books = books
    def __str__(self):
        return f"BookShelf with {len(self.books)} books."

class Book(BookShelf):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Book {self.name}"
book = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book, book2)
print(shelf)

# Type hinting

from typing import List # can be tuple, set, etc.
def list_avg(sequence: List) -> float: # sequence must be a list, makes sure the function returns a float
    return sum(sequence) / len(sequence)
print(list_avg([1, 2, 3]))
# key benefit is that it will tell you if you pass the right thing
# can typehint within arguments like from class and init methods

# Imports

def divide(dividend, divisor):
    return dividend/divisor
print("mymodule.py: ", __name__)

# from mymodule import divide # mymodule is a file, divide is what we want to import
# import mymodule # used to import things non-specifically
# print(divide(10, 2))
# print(__name__)
# import sys # will unlock certain functionalitites
# print(sys.path) # will find paths, usually the first one is the one you're in
# recommend creating a __init__ python file because it's sometimes required
# print(sys.modules) can check what has been imported

# Relative import

# check the Udemy video https://specs.udemy.com/course/complete-python-postgresql-database-course/learn/lecture/19651780#content
# try to just use absolute imports

# Errors in Python

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.") # creating another class here
    return dividend / divisor
grades = []
print("welcome to the average grade program.")
try:
    average = divide(sum(grades), len(grades)) # length is zero which triggers the raise
except ZeroDivisionError as e: # acts as a catch, can find multiple exceptions
    print(e) # prints the ZeroDivisionError above
    print("There are no grades yet in your list.")
else:
    print(f"The average is {average}.") # no error happened will run this
finally:
    print("Thank you!") # should always have a finally despite having errors

# Custom error classes

class TooManyPagesReadError(ValueError): # inherits from an existing error/exception class so it can be raised
    pass # doesn't need to do much inside it, basically a copy of ValueError with a better name

class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0
    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>"
        )
    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {self.pages_read + pages} pages, but this book only has {self.page_count} pages."
            )
        self.pages_read += pages
        print(f"You have now read {self.pages_read} pages out of {self.page_count}.")
python101 = Book("Python 101", 50)
python101.read(35)
# python101.read(50) # will error because there's not 35+50 pages aka 80 pages

# First-class functions

def calculate(*values, operator):
    return operator(*values) # having the () will have operator be read as a function, the function named when invoking
result = calculate(20, 4, operator=divide) # divide is read as the previous function divide from another module

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
        raise RuntimeError(f"Could not find an element with {expected}.")
friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
]
def get_friend_name(friend):
    return friend["name"]
# print(search(friends, "Bob Smith", get_friend_name)) # Will trigger the RuntimeError
print(search(friends, "Rolf Smith", get_friend_name))
print(search(friends, "Rolf Smith", lambda friend: friend["name"])) # lambda function example


# Simple decorators

user = {"username": "jose", "access_level": "guest"}
def get_admin_password():
    return "1234"
# if user["access_level"] == "admin":  # although this is valid, it is
#    print(get_admin_password())       # NOT PROTECTED, would not use
def make_secure(func):
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}."
    return secure_function
get_admin_password = make_secure(get_admin_password)
user = {"username": "jose", "access_level": "admin"} # this line is just to see if the password is sent as an admin
print(get_admin_password) # needs ot be invoked after line 582


# 'at' syntax for decorators

# putting @make_secure before line 574 will prevent hte function from being created as is and will be created and passed through the decorator in one go
# get_admin_password will no longer be registered as a function INTERNALLY, secure_function will be instead
# get_admin_password.__name__ will be secure_function, which can lose some documentation for the user
# we can put the following before declaring secure_function to say it's a wrapper for the func argument:
# @functools.wraps(func)
# but we must import functools before it, this will keep the name documentation
# make_secure is the decorator, secure_function is NOT, but it is wrapped

# Parameters

@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"
print(get_password("billing")) # this will take one argument for panel but will need argument collectors for the previous functions

# Decorators with parameters

# check https://specs.udemy.com/course/complete-python-postgresql-database-course/learn/lecture/19651836#content
# will need to play around and change previous code for this to work

# Mutability

a = [] # a is a list
b = a # b is aliased as a
a.append(35) # adds 35 to the end of the list
print(a) # will be [35]
print(id(a))
print(b) # will also show [35]
print(id(b)) # will show that they are the same object
a = []
b = []
print(id(a)) 
print(id(b)) # will show that b is now different despite showing the same info
# being able to change a list means it is mutable
# in python, all things are mutables because they're all objects unless they are specifically no ways of changing the properties of the objects themselves
a = () # a will be a tuple, you cannot add or remove from a tuple
b = () # cannot append these!
print(id(a))
a = a + (15,) # creates a new tuple, not modify the one before
print(a)
print(id(a)) # shows the id of the new tuple
a = 80
b = 80
print(id(a))
print(id(b)) # integers won't be recreated, it will be the same id, integers are IMMUTABLE
a = 8598 # only a is changed, so b will not be changed
print(f"{a} and {b}") # shows how b is not changed
a = "hello"
b = a
a += " world" # changes a, not string hello necessarily
print(a) # hello world
print(b) # hello

# Mutable default parameteres (and why they're bad)

# Do NOT make parameters equal to a mutable value by default
class Student:
    def __init__(self, name: str, grades: List[int] = []):
        self.name = name
        self.grades = grades
    def take_exam(self, result: int):
        self.grades.append(result)
bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades) # will show that rolf shares the grades
# when the class is created, the function is defined and the default value is created
# SOLUTION: make List[int] = None and make self.grades = grades or []
