# The for Loop
colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    print(color)

# Other Iterable Types
point = (2.1, 3.2, 7.6)
for value in point:
    print(value)

ages = {'kevin': 59, 'bob': 40, 'kayla': 21}
for key in ages:
    print(key)
for key, value in ages.items():
    print(key, value)

for letter in "my_string":
    print(letter)
