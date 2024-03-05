def median(ns):
    total = 0
    for i in ns:
        total += i
    return total / len(ns)

ns = [10,5,10,5]
print(median(ns))