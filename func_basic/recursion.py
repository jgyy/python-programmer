# Solving Problems with Recursion
print("f(n) = f(n-2) + f(n-1)\n")

def fib_exp(n, p="", l=[]):
    old = l
    new = []
    if n <= 1:
        return f"f({n}) = {n}"
    elif not old:
        new = [n - 2, n - 1]
        p += f"f({n}) = f({new[0]}) + f({new[1]})\n"
        return fib_exp(n, p, new)
    if max(old) == 1:
        return p
    for num in old:
        if num > 1:
            new.append(num - 2)
            new.append(num - 1)
        else:
            new.append(num)
    p += f"f({n}) = "
    for num in new:
        if num > 1:
            p += f"f({num}) + "
    p += str(sum(filter(fil, new))) + "\n"

    return fib_exp(n, p, new)

def fil(x):
    if x > 1:
        return False
    else:
        return True

def fib(n):
    nine = {
        0: 0,
        1: 1,
        2: 1,
        3: 2,
        4: 3,
        5: 5,
        6: 8,
        7: 13,
        8: 21,
        9: 34,
    }
    number = nine.get(n, "")
    if type(number) == int:
        return number

    return fib(n - 2) + fib(n - 1)

item_to_calculate = int(input("What Fibonnaci item would you like to calculate? "))

# print(fib_exp(item_to_calculate))
print(fib(item_to_calculate))
