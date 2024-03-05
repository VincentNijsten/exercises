def create_dictionary(keys,values):
    dict = {}
    for i in keys:
        for j in values:
            dict[i] = j
    return dict

print(create_dictionary(['a', 'b', 'c'], [1, 2, 3]))
