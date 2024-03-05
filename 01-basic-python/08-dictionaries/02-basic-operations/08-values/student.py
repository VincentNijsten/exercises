def values(dictionary):
    list = []
    for values in dictionary.values():
        list.append(values)
    return list

dictionary = {"een": 1, "twee":2}
print(values(dictionary))