def contains_duplicates(list):
    x = set()
    for i in list:
        x.add(i)

    if len(list) > len(x):
        return True
    return False

print(contains_duplicates([1,2,2,3,4]))