# Function Basics
def hello_world():
    print("Hello, World!")

hello_world()

def print_name(name):
    print(f"Name is {name}")

print_name("Keith")
output = print_name("Keith")
print(output)

def add_two(num):
    return num + 2

result = add_two(2)
print(result)

# Working with Multiple Parameters
def add(num1, num2):
    return num1 + num2

result = add(1, 5)
print(result)
