def indices_of(xs, condition):
    newList = []
    for i in range(len(xs)):
        if condition(xs[i]):
            newList.append(i)
    return newList