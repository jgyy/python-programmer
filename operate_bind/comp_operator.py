# The Greater Than and Less Than Operators
a = 'a'
one = 1
two = 2
print(1 < 2)
print(2 > 1)
print(2 < 1)
print(1 <= one)
print(2.0 >= 3)

print('a' > 'b')
print('b' > 'a')
print('bb' >= 'ba')
print('a' <= 'c')

# The Equals Operators
print(1 == int('1'))
print(1.0 == 1)
print(2 == 1.0)
print('a' == two)
print('a' == a)

print(1 != one)
print(1.0 != 1)
print(2 != 1.0)
print('a' != two)
print('a' != a)

# The Identity Operators
"""
>>> 1 is 1
True
>>> 1 is 1.0
False
>>> 'a' is 'a'
True
>>> 'a' is not 'b'
True
>>> 'a' is not 'a'
False
>>> [] is []
False
"""

print(id('a'))
print(id('a'))
# print(id('a') == id('a'))
