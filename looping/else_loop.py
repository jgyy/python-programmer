# The else Clause
counter = 1
while counter <= 5:
    print(counter)
    counter += 1
    if counter >= 5:
        break
else:
    print("While loop completed")
for i in [1, 2, 3, 4, 5, 6]:
    print(i)
    if i >= 6:
        break
else:
    print("For loop completed")

colors = ['red', 'pink', 'blue', 'orange', 'green']
for color in colors:
    if color == 'orange':
        print("Orange is in the list")
        break
else:
    print("Orange is not in the list")
