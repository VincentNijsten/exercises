def keys(dictionary):
    list = []
    for keys in dictionary.keys():
        list.append(keys)
    return list

dictionary = {"een": 1, "twee":2}
print(keys(dictionary))