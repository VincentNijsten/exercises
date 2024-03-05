def is_increasing(ns):
    for i in range(len(ns) - 1):
        if ns[i] > ns[i + 1]:
            return False
    return True

# Test cases
print(is_increasing([1, 2, 3, 4, 4, 7]))  # True
print(is_increasing([1, 3, 2, 4]))        # False
