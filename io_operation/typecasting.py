# Converting from a Number Type to a Number Type
print(float(1))
print(int(1.3))
print(int(2.6))

# Converting to and from a String
print(str(1))
print(str(2.6))
print(str(False))
print(int('1'))
print(float('1'))
print(float('1.2'))

# Converting to a Boolean
print(bool(1))
print(bool(2.4))
print(bool('Tada'))
print(bool('Tada'.lower))
print(bool(0))
print(bool(0.0))
print(bool(""))

# Boolean Operators with Non-Boolean Objects
zero_int = 0
zero_float = 0.0
one = 1
this = 'This'
print(one and 0)
print(this and 'That')
print(this and zero_int and 'That')
print(zero_float and 1)
print(one or 0)
print(zero_int or 1)
print(zero_int or "")
print(zero_int or one or 'This')
print(not "")
print(not 1)
