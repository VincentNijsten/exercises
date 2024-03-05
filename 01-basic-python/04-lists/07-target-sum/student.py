def target_sum(ns, target):
    for x in ns:
        for y in ns:
            if x + y == target:
                return True
    return False
print(target_sum([1, 2, 3], 5)) # True --> 2 + 3 = 5
print(target_sum([1, 2, 3], 7)) # False --> 7 is niet te krijgen met 2 getallen