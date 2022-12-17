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