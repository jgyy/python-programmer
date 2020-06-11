# List Methods
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
my_list.insert(0, 'a')
print(my_list)
my_list = [1, 2, 3]
print(my_list.index(2))

# The in and not in Operators
my_list = [1, 2, 3]
print(4 in my_list)
print(4 not in my_list)
print(2 in my_list)

# Helpful Functions
my_list = [1, 3, 4, 8, 2]
print(sorted(my_list))
print(reversed(my_list))
print(list(reversed(my_list)))
print(list(reversed(sorted(my_list))))
