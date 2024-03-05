def keys_with_value(dictionary, values):
    list = []
    for key, value in dictionary.items():
        if value == values:
            list.append(key)
    return list

dictionary = {'a': 1, 'b': 2, 'c': 1}
print(keys_with_value(dictionary, 1))