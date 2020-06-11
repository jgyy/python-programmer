# Name Hiding in Action
y = 5

def set_x(y):
    print("Inner y:", y)
    x = y
    y = x
    print("Inner y:", y)

set_x(10)
print("Outer y:", y)
