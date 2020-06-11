# Dictionaries
ages = { 'kevin': 59, 'alex': 29, 'bob': 40 }
print(ages)
print(ages['kevin'])
ages['kayla'] = 21
print(ages)
del ages['kevin']
print(ages)
del ages

# The in and not in Operators
ages = {'kevin': 59, 'bob': 40}
print('kevin' in ages)
print(59 in ages)

# Alternative Ways to Create a dict Using Keyword Arguments
weights = dict(kevin=160, bob=240, kayla=135)
print(weights)
colors = dict([('kevin', 'blue'), ('bob', 'green'), ('kayla', 'red')])
print(colors)
