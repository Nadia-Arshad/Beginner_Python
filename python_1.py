# Tip no. 1
# - Assigning values to different variables in one line:
a, b = 5, 10
print(a + b)

# Tip no. 2
# - To use a different color in terminal for text.
print("\033[96mThis is a different color.")

# Tip no. 3
# - Instead of using multiple stars just take the power.
print(5*5*5*5*5*5*5*5)
print(5**8)

# Tip no. 4
# - Rounding Off
print(round(10.5))
print(round(11.5))    #Round function rounds off to the even number.

# Tip no. 5
# - Split large numbers using underscore

num_1 = 444_555_666_888_887
print(num_1)

# Tip no. 6
# - Open websites from code. 

import webbrowser
webbrowser.open('https://www.desmos.com')

# Tip no. 7
# - Multiline Strings:

print("This is a girl,\
 and that there is a boy.")

# Tip no. 8 
# - Reverse a list

num_list = [9, 7, 5, 3, 1]
print(num_list[::-1])   #-1 gets the last index, :: will tell it to take everyone.

# Or you can use .reverse() method 
num_list.reverse()
print(num_list)

# Tip no. 9
# Look for something

if "and" in "standard":
    print("standard".index("and"))

# OR

print("standard".find("and"))

# Tip no. 10
# Copying 

data_1 = {"Madi" : 8}
data_2 = data_1
print(id(data_1))
print(id(data_2))
data_2 ["Evan"] = 23
print(data_2)

#Since both variables are pointing towards the same memory location, change in one will change the other too. 

data_00 = 5
data_01 = data_00
data_00 = 10
# For primitive data types, it will point towards different memory locations, and won't be the same.
print(id(data_00))
print(id(data_01))


#.copy() method

lan = ["Spanish", "English", "Urdu", "Swahili"]
lan_1 =  lan.copy()
print(id(lan))
print(id(lan_1))

lan [0] = "French"
print(lan)
print(lan_1)

#variables pointing at different locations stay separate and modification in one doesn't effect the other.

#One more way of making a copy but that points to the same memory location

jobs = ["CS", "operator", "manager", ["delivery boy", "waiter", "receptionist"]]
job_1 =  jobs[:]
print(id(jobs), id(job_1))
job_1 [-1][-1] = "porter"
print(jobs)

#To prevent it we us deepcopy

from copy import deepcopy

job_1 = deepcopy(jobs)
print(id(jobs), id(job_1))
job_1 [-1][-1] = "porter"
print(jobs)

# Tip no. 11
# - Joining two lists with + sign

beginning = [1, 2, 3, 4, 5]
ending = [6, 7, 8, 9, 10]
print(beginning + ending)

# Tip no. 12
#Assigning values through function

def get_position():
    #get data
    return 5, 10, 15, 20

x, y, z, a = get_position()
print(a, y, x, z)


# Tip no. 12
# - if else in one line
reputation = 20
status = None
if reputation > 15:
    status = "Admin"
else:
    status = "User"
print(status)
#Replace it with:

status = "Admin" if reputation > 15 else "User"
print(status)

# Tip np. 13
# Checking for value in a list

people = ["man", "woman", "girl", "boy", "baby", "dogs", "cats", "chihuahuas"]
if "cats" in people:
    print("WOW")

# Tip no. 14
# Print a list of numbers using range

numbers = list(range(20))
print(numbers)

# Tip no. 15
# - Unpacking

def move_positions(x, y, z):
    print(f"Moving Numbers to {x}, {y}, {z}")

data = [5, 10, 15]
move_positions(*data)   # This is equivalent to saying data[0], data[1], data[2]


# Tip no. 16
# - To get one unique element from a list where duplicate values exits but then order won't be the same.

pets = ["cat", "dog", "mouse", "cat", "horse", "cow", "cow", "dog"]
print(set(pets))
print(list(set(pets)))    #convert it to set, then pass it to list constructor to again get back the list.

# Tip no. 17
# Checking multiple conditions in a loop: Make a list

traits = "naughty"
list_t = ["jealous", "egoistic", "naughty", "disrespectful"]
if traits in list_t:
    print("Don't be friends!")


# Tip no. 18
# Use of "any" and "all"

age = 25
reputation = 20
if age >= 21 and reputation >= 20:
    status = "Admin"
else:
    status = "User"

#We can now replace the if line with multiple conditions with a list
age = 50
reputation = 24

conditions = [
    age >= 25,
    reputation >=20
]

if all(conditions):
    print("Admin")
else:
    "User"

# Tip no. 19
# How .split() works
# This way we can take multiple data and store it at different locations.

full_name = input("What is your full name? ")
print(full_name.split())    # It is creating a list
f_name, l_name = (full_name.split())   # This is assigning each element to a unique variable
print(f_name, l_name)

# Tip no. 20
# We can not use " ".join() to flip what we did earlier. 

name = ["Nadia", "Arshad"]
full_name = " ".join(name)    
print(full_name)


#Tip no. 21
# Reverse print a loop

pets = ["dog", "cat", "chicken", "cow", "horse", "parrot", "snake", "spider"]
for pet in reversed(pets):
    print(pet)


# Tip no. 22 
# - Keeping the desired pets  -  List Comprehension
pets = ["dog", "cat", "chicken", "cow", "horse", "parrot", "snake", "spider"]
no_pets = [pet for pet in pets if pet not in ["chicken", "parrot", "cow"]]
print(no_pets)

# Top no. 23
# How to use time.sleep

import time
def done():
    time.sleep(7)
    print("done")

done()


# Tip no. 24
# To print the index through iteration

pets = ["dog", "cat", "chicken", "cow", "horse", "parrot", "snake", "spider"]
for i, pet in enumerate(pets):
    print(i, pet)


# Tip no. 25
# - Flattening the nested lists

numbers = [[1, 2], [3, 4], [5, 6]]
flat = []
for number in numbers:
    for item in number:
        flat.append(item)
print(flat)

#Or using list comprehension

flat = [item for number in numbers for item in number]
print(flat)


#Voila Done! :) 