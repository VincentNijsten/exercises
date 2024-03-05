def includes(xs, ys):
    for x in xs:
        for y in ys:
            if x == y:
                return True
    return False

print(includes([1, 2, 3], [7, 4]))