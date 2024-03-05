def target_sum(ns, target):
    for x in ns:
        for y in ns:
            if x + y == target and x != y:
                return True
    return False

print(target_sum([1, 2, 3], 6))  # False
print(target_sum([1, 2, 3, 3], 6))  # True

# Werkt niet