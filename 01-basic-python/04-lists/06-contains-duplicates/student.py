def contains_duplicates(xs):
    dubbles = []
    for i in xs:
        if i not in dubbles:
            dubbles.append(i)

    if len(xs) > len(dubbles):
        return 'Er zitten dubbels in'
    elif len(xs) == len(dubbles):
        return 'Er zitten geen dubbels in'

xs = [1,1,2,5]
print(contains_duplicates(xs))