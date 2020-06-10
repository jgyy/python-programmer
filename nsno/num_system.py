# Number Systems
def div(num, den):
    divison = f"{num} / {den}"
    floor = str(num // den)
    modulo = str(num % den)
    return f"{divison} > {floor} w/ remainder of {modulo}"

values = [(15, 2), (7, 2), (3, 2), (1, 2), (12, 2), (6, 2), (3, 2), (1, 2)]
for val in values:
    print(div(*val))

def convert(nums):
    ps = ""
    final = 0
    for num in nums:
        ps += f"({num[0]} * {num[1]} ^ {num[2]}) + "
    ps = ps[:-3] + "\n"
    for num in nums:
        exponent = num[1] ** num[2]
        ps += f"({num[0]} * {exponent}) + "
    ps = ps[:-3] + "\n"
    for num in nums:
        multiply = num[0] * (num[1] ** num[2])
        ps += f"{multiply} + "
    ps = ps[:-3] + "\n"
    for num in nums:
        final += num[0] * (num[1] ** num[2])
    ps += str(final)
    return ps

value = [(1, 2, 3), (1, 2, 2), (0, 2, 1), (0, 2, 0)]
print(convert(value))

print(0b1001)
print(0o7424)
print(0xFF012)

print(bin(10))
print(oct(59))
print(hex(1024))
