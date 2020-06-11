# Writing a Generator Function
def gen_range(stop, start=1, step=1):
    num = start
    while num <= stop:
        yield num
        num += step

print(gen_range(10))
generator = gen_range(4)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

for num in gen_range(10, step=2):
    print(num)
