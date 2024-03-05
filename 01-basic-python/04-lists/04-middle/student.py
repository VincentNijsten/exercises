from math import floor

def middle(ns):
    index = floor(len(ns)/2)
    return ns[index]

print(middle([1,2,3,4,5]))