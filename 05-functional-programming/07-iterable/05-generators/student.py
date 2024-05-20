def repeat(value):
    current = value
    while True:
        yield current

xs = repeat(5)
print(next(xs)) # 5
print(next(xs)) # 5