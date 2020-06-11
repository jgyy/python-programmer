# Writing a Generator Function
def gen_range(stop, start=1, step=1):
    num = start
    while num <= stop:
        yield num
        num += step

def gen_fib():
    a, b, c = 0, 1, 0
    while c < 1024:
        a, b, c = b, a + b, c + 1
        yield (c, a)

print(gen_range(10))
generator = gen_range(4)
print(list(generator))

for num in gen_range(10, step=2):
    print(num)

# Converting a Generator to a List
generator = gen_range(10)
print(list(generator))

fib = gen_fib()
print(list(fib))
