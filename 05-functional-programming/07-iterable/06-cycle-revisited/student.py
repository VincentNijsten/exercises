import itertools

def cycle(xs):
    while True:
        for value in xs:
            yield value

xs = cycle('abcd')
result = itertools.islice(xs, 10)
print(list(result))