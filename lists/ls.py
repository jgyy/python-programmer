# Lists
my_list = [1, 2, 3, 4, 5]
other_list = ['a', 1, 1.0, False]

# Reading from Lists
print(my_list[0])
print(my_list[2])
print(len(my_list))
print(my_list[0:2])
print(my_list[1:0])
print(my_list[:3])
print(my_list[0::1])
print(my_list[0::2])

# Modifying a List
my_list[0] = "a"
print(my_list)
print(my_list + [8, 9, 10])
my_list += [8, 9, 10]
print(my_list)
my_list[1:3] = ['b', 'c']
print(my_list)
my_list[3:5] = ['d', 'e', 'f']
print(my_list)
my_list = ['a', 'b', 'c', 'd', 5, 6, 7]
my_list[4:] = []
print(my_list)

# Removing Items from a List
my_list = ['a', 'b', 'c', 'd']
del my_list[0]
print(my_list)
del my_list
