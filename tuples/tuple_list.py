# Tuples vs Lists
person = ('Kevin Bacon', 61, '555-555-5555')
person2 = ('Bob Ross', 76, '')
print(person[0])
print(person2[0])

# Lists in Tuples and Tuples in Lists
my_list = [1, 2, 3]
my_tuple = (my_list, 1)
print(my_tuple)
other_list = [1, 2, my_tuple]
print(other_list)
print(my_tuple)
my_list.append(1)
print(my_tuple)
