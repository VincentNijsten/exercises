def rotate(xs, n):
    for i in range(n):
        xs.append(xs[0])
        del xs[0]
    print(xs)

xs = [1, 2, 3, 4, 5]
n = 2
rotate(xs, n)
