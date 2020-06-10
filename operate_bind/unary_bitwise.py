# Operators: Bitwise Complement
a = 0b010
print(a)
print(bin(a))
print(~a)
print(bin(~a))

# Bitwise OR
a = 0b1001
b = 0b1100
print(bin(a | b))

# Bitwise AND
a = 0b1001
b = 0b1100
print(bin(a & b))

# Bitwise XOR
a = 0b1001
b = 0b1100
print(bin(a ^ b))

# Bitwise Right Shift
a = 0b110
print(bin(a >> 2))
print(bin(a >> 4))

# Bitwise Left Shift
a = 0b110
print(bin(a << 2))
print(bin(a << 4))
