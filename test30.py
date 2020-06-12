# Which of the following lines of code would set the third value in the names list to be 'Jimmy'? Here's the starting value for names:
names = ['Alice', 'Bob', 'Lance', 'Mike']
print(names)

# What is the output of this code?
num1 = 15
num2 = num1
num1 *= 2
print(num2)

# "#" is used to create a single-line comment.

# '7.2' and 'Test' is a string?

# What would be the value of the all_names variable after running this code?
names = ['Alice', 'Lance', 'Bob', 'Mike']
all_names = names
names.append('Brock')
print(all_names)

# '//' is the floor division operator.

# What is the output of this code?
num = 1
while num <= 6:
    if num % 3 == 0:
        print(num)
    num += 1

# What is the output of the following code?
def double_values(list1):
    doubles = []
    for num in list1:
        doubles.append(num * 2)

first_list = [1, 2, 3, 4]
print(double_values(first_list))

# Which of these print lines would print the expected output, given the input values:
# Input Values: "1600 Pennsylvania Ave NW", "Washington", "DC"
# Expected Output: 1600 Pennsylvania Ave NW, Washington, DC
print("1600 Pennsylvania Ave NW", "Washington", "DC", sep=', ')

# What would be the value of names after running this code?
names = ['Alice', 'Bob', 'Lance', 'Mike']
names = names[::-1]
print(names)

# What is the output of this code?
num1 = 30
num2 = 15
print(num2 == num1)

# What code would result in the expected output when inserted into the commented line?
# Expected Output: False
values = ['Kevin Bacon', 60, '555-555-5555', False]
val = not values[1]
print(val)

# '%' is the modulus operator.

# What would be the value of all_names after running this code?
names = ['Alice', 'Bob', 'Lance', 'Mike']
all_names = names
names.remove('Bob')
print(all_names)

# There are no block comments in Python.

# What is the output of this code?
pair1 = ('a', 'b', 'c')
pair2 = ('d', 'e', 'f')
index = 0

while index < len(pair1):
    for item in pair2:
        print(pair2[index], item)
    index += 1

# What is the output of this code?
letter = 'a'
if letter < 'b':
    print("First")
if letter == 'b' or letter > 'c':
    print("Second")
elif letter <= 'a':
    print("Third")
else:
    print("Fourth")

# What is the output of the following code?
def double_values(list1):
    doubles = []
    for num in list1:
        doubles.append(str(num * 2))
    return doubles

first_list = [1, 2, 3, 4]
print(" ".join(double_values(first_list)))

# What argument to the hello function would lead to the expected output?
# Expected Output: Howdy, William
def hello(name, salutation):
    print(salutation, name, sep=", ")

hello(name="William", salutation="Howdy")

# What does the following code evaluate to?
print(3 ** 3)

# Which of these statements is true?
# The yield keyword is used to state that a function is a generator.
# A function is created using the def keyword.

# True is a Boolean.

# What is the output of the following code?
def add_five(num1, num2=5):
    return num1 + 5
print(add_five(1, 2))

# What argument to the hello function would lead to the expected output?
# Expected Output: Howdy, Oscar!
def hello(name, salutation):
    print(salutation, name, sep=", ")

hello(salutation="Howdy",name="Oscar!")
