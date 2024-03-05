def add_indices(xs):
    indices = range(len(xs))
    return list(zip(indices, xs))

print(add_indices([7,4,9]))