# Modifying the Global State from a Nested Scope
y = 5
a = 7

def set_x(z):
    x = z
    global y
    global a
    y = x
    a = 7

print("y Before set_x:", y)
set_x(10)
print("y After set_x:", y)
print("a After set_x:", a)
